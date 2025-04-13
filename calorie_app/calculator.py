from flask import (
    Blueprint, request, render_template, flash
)
from categories.calorie_calculator import calculate_calories

bp = Blueprint('calculator', __name__, '/')


@bp.route('/calculate', methods=['GET', 'POST'])
def calculate():
    total_calories = 0
    if request.method == 'POST':
        ingredient_list = request.form.get('ingredients', '').replace(', ', ',').split(',')
        portions = request.form.get('portions', '').replace(', ', ',').split(',')
        meal = {}
        try:
            for i in range(len(ingredient_list)):
                meal[ingredient_list[i]] = {
                    "grams": portions[i]
                }
        except Exception as e:
            flash(f"Error: {e}")
        
        total_calories = calculate_calories(meal)
    
    return render_template('calculator.html', meal_calories=total_calories)