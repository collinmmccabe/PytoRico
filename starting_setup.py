# First int key is for number of players, second int key is for index of player in player list
player_init = {
    2: {
        0: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    3: {
        0: {
            'doubloons': 2,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 2,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 2,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    4: {
        0: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 3,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        },
        3: {
            'doubloons': 3,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    5: {
        0: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 4,
            'first_plantation': 'indigo',
            'governor': False
        },
        3: {
            'doubloons': 4,
            'first_plantation': 'corn',
            'governor': False
        },
        4: {
            'doubloons': 4,
            'first_plantation': 'corn',
            'governor': False
        }
    },
    6: {
        0: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': True
        },
        1: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': False
        },
        2: {
            'doubloons': 5,
            'first_plantation': 'indigo',
            'governor': False
        },
        3: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        },
        4: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        },
        5: {
            'doubloons': 5,
            'first_plantation': 'corn',
            'governor': False
        }
    },
}

# Plantation tile counts assume that the starting tiles have already been taken out for players
# int keys are for the number of players
setup_dict = {
    2: {
        'colonists': 42, 
        'vp': 65, 
        'barrel_dict': {
            'corn': 8,
            'indigo': 9,
            'sugar': 9,
            'tobacco': 7,
            'coffee': 7 }, 
        'plantation_dict': {
            'corn': 6,
            'indigo': 8,
            'sugar': 8,
            'tobacco': 6,
            'coffee': 5 },
        'quarries': 5,
        'building_dict': {
            'small_indigo_plant': 2,
            'small_sugar_mill': 2,
            'indigo_plant': 2,
            'sugar_mill': 2,
            'tobacco_storage': 2,
            'coffee_roaster': 2,
            'small_market': 1,
            'hacienda': 1,
            'construction_hut': 1,
            'small_warehouse': 1,
            'hospice': 1,
            'office': 1,
            'large_market': 1,
            'large_warehouse': 1,
            'factory': 1,
            'university': 1,
            'harbour': 1,
            'wharf': 1,
            'guild_hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs_house': 1,
            'city_hall': 1
             }, 
        'prospectors': 1,
        'ship_size_list': [4, 6]
    },
    3: {
        'colonists': 58, 
        'vp': 75, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 9,
            'indigo': 10,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small_indigo_plant': 3,
            'small_sugar_mill': 3,
            'indigo_plant': 3,
            'sugar_mill': 3,
            'tobacco_storage': 3,
            'coffee_roaster': 3,
            'small_market': 2,
            'hacienda': 2,
            'construction_hut': 2,
            'small_warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large_market': 2,
            'large_warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild_hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs_house': 1,
            'city_hall': 1 },  
        'prospectors': 0,
        'ship_size_list': [4, 5, 6]
    },
    4: {
        'colonists': 79, 
        'vp': 100, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 8,
            'indigo': 10,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small_indigo_plant': 4,
            'small_sugar_mill': 4,
            'indigo_plant': 3,
            'sugar_mill': 3,
            'tobacco_storage': 3,
            'coffee_roaster': 3,
            'small_market': 2,
            'hacienda': 2,
            'construction_hut': 2,
            'small_warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large_market': 2,
            'large_warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild_hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs_house': 1,
            'city_hall': 1 }, 
        'prospectors': 1,
        'ship_size_list': [5, 6, 7] 
    },
    5: {
        'colonists': 100, 
        'vp': 122, 
        'barrel_dict': {
            'corn': 10,
            'indigo': 11,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 9 }, 
        'plantation_dict': {
            'corn': 8,
            'indigo': 9,
            'sugar': 11,
            'tobacco': 9,
            'coffee': 8 },
        'quarries': 8,
        'building_dict': {
            'small_indigo_plant': 4,
            'small_sugar_mill': 4,
            'indigo_plant': 3,
            'sugar_mill': 3,
            'tobacco_storage': 3,
            'coffee_roaster': 3,
            'small_market': 2,
            'hacienda': 2,
            'construction_hut': 2,
            'small_warehouse': 2,
            'hospice': 2,
            'office': 2,
            'large_market': 2,
            'large_warehouse': 2,
            'factory': 2,
            'university': 2,
            'harbour': 2,
            'wharf': 2,
            'guild_hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs_house': 1,
            'city_hall': 1 },
        'prospectors': 2,
        'ship_size_list': [6, 7, 8] 
    },
    6: {
        'colonists': 121, 
        'vp': 150, 
        'barrel_dict': {
            'corn': 12,
            'indigo': 14,
            'sugar': 14,
            'tobacco': 11,
            'coffee': 11 }, 
        'plantation_dict': {
            'corn': 9,
            'indigo': 12,
            'sugar': 14,
            'tobacco': 11,
            'coffee': 10 },
        'quarries': 10,
        'building_dict': {
            'small_indigo_plant': 5,
            'small_sugar_mill': 5,
            'indigo_plant': 4,
            'sugar_mill': 4,
            'tobacco_storage': 4,
            'coffee_roaster': 4,
            'small_market': 3,
            'hacienda': 3,
            'construction_hut': 3,
            'small_warehouse': 3,
            'hospice': 3,
            'office': 3,
            'large_market': 3,
            'large_warehouse': 3,
            'factory': 3,
            'university': 3,
            'harbour': 3,
            'wharf': 3,
            'guild_hall': 1,
            'residence': 1,
            'fortress': 1,
            'customs_house': 1,
            'city_hall': 1 },
        'prospectors': 3,
        'ship_size_list': [7, 8, 9]
    }
}