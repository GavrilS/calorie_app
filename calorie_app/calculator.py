from flask import (
    Blueprint, request, render_template, flash
)
from categories import calorie_calculator

bp = Blueprint('calculator', __name__, '/')


@bp.route('/calculate', methods=['GET', 'POST'])
def calculate():
    total_calories = 0
    if request.method == 'POST':
        ingredient_list = request.form.get('ingredients', [])
        portions = request.form.get('portions', [])
        meal = {}
        try:
            for i in range(len(ingredient_list)):
                meal[ingredient_list.get(i)] = {
                    "grams": portions.get(i)
                }
        except Exception as e:
            flash(f"Error: {e}")
        
        total_calories = calorie_calculator(meal)
    
    return render_template('calculator', total_calories)