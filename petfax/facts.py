
from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts.html')

@bp.route("/" , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/facts')
    return render_template('/facts/index.html')