"""
A helper to calculate calories from lists of user supplied ingredients/meals.
"""
from meats import meat_list
from vegetables import vegetable_list

def calculate_calories(meal):
    total_calories = 0
    for item in meal.items():
        print(item)


def _calories_per_portion(ingredient, portion_grams, category):
    if 'meat' in category:
        source = meat_list
    else:
        source = vegetable_list
    
    grams = source.get(ingredient).get('measurement')
    calories = source.get(ingredient).get('calories')
    total_calories = calories * (portion_grams / grams)
    return total_calories


if __name__=='__main__':
    meal = {
        'steak': 250,
        'chicken breast': 100,
        'cauliflower': 200
    }

    calculate_calories(meal)