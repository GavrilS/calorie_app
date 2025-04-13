"""
A helper to calculate calories from lists of user supplied ingredients/meals.
"""
import math
from categories.meats import meat_list
from categories.vegetables import vegetable_list

def calculate_calories(meal):
    total_calories = 0
    errors = []
    for item, value in meal.items():
        try:
            total_calories += _calories_per_portion(item, int(value.get('grams')))
        except Exception as e:
            print(f"Exception for {item}: {e}")
            errors.append(item)
    
    return math.ceil(total_calories), errors


def _calories_per_portion(ingredient, portion_grams):
    if ingredient in meat_list:
        source = meat_list
    else:
        source = vegetable_list
    
    grams = source.get(ingredient, {}).get('measurment', 0)
    calories = source.get(ingredient, {}).get('calories', 0)

    total_calories = calories * (portion_grams / grams)
    return total_calories
