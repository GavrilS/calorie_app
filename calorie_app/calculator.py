from flask import (
    Blueprint, request, render_template
)
from categories import calorie_calculator

bp = Blueprint('calculator', __name__, '/')


@bp.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        pass
    
    return render_template('calculator')