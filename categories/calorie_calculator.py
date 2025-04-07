"""
A helper to calculate calories from lists of user supplied ingredients/meals.
"""
from meats import meat_list
from vegetables import vegetable_list

def calculate_calories(meal):
    for item in meal.items():
        print(item)


if __name__=='__main__':
    meal = {
        'steak': 250,
        'chicken breast': 100,
        'cauliflower': 200
    }

    calculate_calories(meal)