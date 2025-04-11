"""
A helper to calculate calories from lists of user supplied ingredients/meals.
"""
import math
from meats import meat_list
from vegetables import vegetable_list

def calculate_calories(meal):
    total_calories = 0
    errors = []
    for item, value in meal.items():
        try:
            total_calories += _calories_per_portion(item, value.get('grams'), value.get('category'))
        except Exception as e:
            print(f"Exception for {item}: {e}")
            errors.append(item)
    
    return math.ceil(total_calories), errors


def _calories_per_portion(ingredient, portion_grams, category):
    if 'meat' in category:
        source = meat_list
    else:
        source = vegetable_list
    
    grams = source.get(ingredient, {}).get('measurment', 0)
    calories = source.get(ingredient, {}).get('calories', 0)

    total_calories = calories * (portion_grams / grams)
    return total_calories


if __name__=='__main__':
    meal = {
        'steak': {'grams': 250, 'category': 'meat'},
        'chicken breast': {'grams': 100, 'category': 'meat'},
        'cauliflower': {'grams': 200, 'category': 'vegetables'}
    }

    print(calculate_calories(meal))