class DictRef(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, value):
        self[key] = value

class Player(object):
    def __init__(self, name, player_init_subdict):
        self.name = name
        self.doubloons = player_init_subdict['doubloons']
        self.vp = 0
        self.free_colonists = 0
        self.governor_flag = player_init_subdict['governor']
        self.island = self.Island(player_init_subdict['first_plantation'])
        self.city = self.City()
        self.supply = self.Barrels()

    class Island(DictRef):
        def __init__(self, first_plantation):
            setattr(self, 'plot_01', self.Plantation(first_plantation))
            for n in range(2, 13):
                setattr(self, 'plot_' + str(n).zfill(2), None)  # i.e. self.plot_01 = Plantation()

        def swap_plots(self, from_plot, to_plot):
            self[from_plot], self[to_plot] = self[to_plot], self[from_plot]
            return None
        def plots_built(self):
            return sum(1 for i in self.values() if i is not None)
        def build(self, island_plot, good_produced):
            if ((self.plots_built() < 12) and (self[island_plot] is None)):
                self[island_plot] = self.Plantation(good_produced)
            return None

        class Plantation(DictRef):
            def __init__(self, good_produced):
                self.good_produced = good_produced
                self.occupied = False
    
    class City(DictRef):
        def __init__(self):
            for n in range(1, 13):
                setattr(self, 'plot_' + str(n).zfill(2), None)  # i.e. self.plot_01 = Building()

        def swap_plots(self, from_plot, to_plot):
            if ((self[from_plot] is not None) and (self[from_plot].size == 2)):
                from_plot_plus_one = 'plot_' + str(int(from_plot[-2:]) + 1).zfill(2)
                to_plot_plus_one = 'plot_' + str(int(to_plot[-2:]) + 1).zfill(2)
                self.move_building(from_plot_plus_one, to_plot_plus_one)
            self[from_plot], self[to_plot] = self[to_plot], self[from_plot]
            return None
        def plots_built(self):
            return sum(1 for i in self.values() if i is not None)
            
        class Building(DictRef):
            def __init__(self, building_lookup):
                self.building_name = building_lookup.name
                self.size = building_lookup.size
                self.good_processed = building_lookup.good_processed
                self.free_worker_spaces = building_lookup.free_worker_spaces
                self.occupied_worker_spaces = 0
    
    class Barrels(DictRef):
        def __init__(self):
            self.corn = 0
            self.indigo = 0
            self.sugar = 0
            self.tobacco = 0
            self.coffee = 0
    
    def lose_doubloons(self, number):
        if self.doubloons >= number:
            self.doubloons -= number
            return number
        return None
    def get_doubloons(self, number):
        self.doubloons += number
        return number
    def get_vp(self, number):
        self.vp += number
        return number
    def get_colonists(self, number):
        self.free_colonists += number
        return None
    def set_governor_flag(self, bool_value):
        self.governor_flag = bool_value
        return None
    
    def add_colonist(self, region, plot):
        if ((region == 'island') and (not self.island[plot].occupied) and (self.free_colonists > 0)):
            self.island[plot].occupied = True
            self.free_colonists -= 1
        elif ((region == 'city') and (self.city[plot].free_worker_spaces > 0) and (self.free_colonists > 0)):
            self.city[plot].occupied_worker_spaces += 1
            self.city[plot].free_worker_spaces -= 1
            self.free_colonists -= 1
        return None
    def remove_colonist(self, region, plot):
        if ((region == 'island') and (self.island[plot].occupied)):
            self.island[plot].occupied = False
            self.free_colonists += 1
        elif ((region == 'city') and (self.city[plot].occupied_worker_spaces > 0)):
            self.city[plot].occupied_worker_spaces -= 1
            self.city[plot].free_worker_spaces += 1
            self.free_colonists += 1
        return None
    
    def produce_plantation(self, market_supply_dict):  # send the market supply here to communicate with fn
        taken = min(sum(1 for i in self.island if (i.good_produced == 'corn' and i.occupied)), market_supply_dict.corn)
        market_supply_dict.corn -= taken
        self.supply.corn += taken
        for good_type in ['indigo', 'sugar', 'tobacco', 'coffee']:  # could replace list with keys of mkt spl d
            taken = min(min(sum(1 for i in self.island if (i.good_produced == good_type and i.occupied)), 
                            sum(j.occupied_worker_spaces for j in self.city if j.good_processed == good_type)), 
                        market_supply_dict[good_type])
            market_supply_dict[good_type] -= taken
            self.supply[good_type] += taken
        # Maybe use return value to communicate with Market class?
        return market_supply_dict
    
    def build_building(self, city_plot, building_lookup, cost):  # specific building lookup is BuildingLookup[building_name]
        endgame_trigger = False
        if ((building_lookup.size + self.city.plots_built() <= 12) and (self.city[city_plot] is None) and
          (building_lookup.name not in [i.building_name for i in self.city if i is not None]) and
          (cost <= self.doubloons)):
            if ((building_lookup.size == 2) and (self.city['plot_' + str(int(city_plot[-2:]) + 1).zfill(2)] is None)):
                self.city['plot_' + str(int(city_plot[-2:]) + 1).zfill(2)] = self.city.Building({
                                                                                'name': 'second plot for large building',
                                                                                'size': 0,
                                                                                'good_processed': None,
                                                                                'free_worker_spaces': 0 })
                self.city[city_plot] = self.city.Building(building_lookup)
            elif building_lookup.size == 1:
                self.city[city_plot] = self.city.Building(building_lookup)
            else:
                return endgame_trigger, None
            if self.city.plots_built() == 12:
                endgame_trigger = True
            return endgame_trigger, self.lose_doubloons(cost)  # Use return value to communicate with Market class
        return endgame_trigger, None

    def ship_resources(self, good, number):
        if self.supply[good] >= number:
            self.supply[good] -= number
            return number, self.get_vp(number)  # this will be used to update Market.Supply[good] and Market.vp
        return None, None
    def trade_resources(self, good):
        trade_value = {'corn': 0, 'indigo': 1, 'sugar': 2, 'tobacco': 3, 'coffee': 4}
        if self.supply[good] > 0:
            self.supply[good] -= 1
            self.get_doubloons(trade_value[good])
            return good  # for TradingPost.trading_queue.append(good)
        return None
    
    def __repr__(self):
        gov_desc = "not " if not self.governor_flag else ""
        return ("\n{} is {}currently the governor.\n\nWEALTH:\n"
                "doubloons: {}, victory points: {}, available colonists: {}\n"
                "\nSUPPLY:\ncorn: {}, indigo: {}, sugar:{}, tobacco: {}, coffee: {}\n"
                "\nISLAND:\nPlot 01: {}\nPlot 02: {}\nPlot 03: {}\nPlot 04: {}\nPlot 05: {}\nPlot 06: {}"
                "\nPlot 07: {}\nPlot 08: {}\nPlot 09: {}\nPlot 10: {}\nPlot 11: {}\nPlot 12: {}\n"
                "\nCITY:\nPlot 01: {}\nPlot 02: {}\nPlot 03: {}\nPlot 04: {}\nPlot 05: {}\nPlot 06: {}"
                "\nPlot 07: {}\nPlot 08: {}\nPlot 09: {}\nPlot 10: {}\nPlot 11: {}\nPlot 12: {}\n".format(self.name,
                                                                                  gov_desc,
                                                                                  str(self.doubloons),
                                                                                  str(self.vp),
                                                                                  str(self.free_colonists),
                                                                                  str(self.supply.corn),
                                                                                  str(self.supply.indigo),
                                                                                  str(self.supply.sugar),
                                                                                  str(self.supply.tobacco),
                                                                                  str(self.supply.coffee),
                                                                                  self.island.plot_01,
                                                                                  self.island.plot_02,
                                                                                  self.island.plot_03,
                                                                                  self.island.plot_04,
                                                                                  self.island.plot_05,
                                                                                  self.island.plot_06,
                                                                                  self.island.plot_07,
                                                                                  self.island.plot_08,
                                                                                  self.island.plot_09,
                                                                                  self.island.plot_10,
                                                                                  self.island.plot_11,
                                                                                  self.island.plot_12,
                                                                                  self.city.plot_01,
                                                                                  self.city.plot_02,
                                                                                  self.city.plot_03,
                                                                                  self.city.plot_04,
                                                                                  self.city.plot_05,
                                                                                  self.city.plot_06,
                                                                                  self.city.plot_07,
                                                                                  self.city.plot_08,
                                                                                  self.city.plot_09,
                                                                                  self.city.plot_10,
                                                                                  self.city.plot_11,
                                                                                  self.city.plot_12))
