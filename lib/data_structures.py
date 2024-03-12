spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food['name'] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spice_level = [food for food in spicy_foods if food['heat_level'] >= 6]
    return spice_level  

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_emoji = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}") 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if(cuisine == food['cuisine']):
            return food
    

def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    if(spiciest_food):
        return print_spicy_foods(spiciest_food)
    

def get_average_heat_level(spicy_foods):
    spice_level = [food['heat_level'] for food in spicy_foods]
    average = sum(spice_level) / len(spice_level)
    return average
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
