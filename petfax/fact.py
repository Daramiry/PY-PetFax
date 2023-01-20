
from flask import ( Blueprint, render_template, redirect, request ) 
from . import models

bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')

@bp.route('/', methods=['GET','POST'])
def index(): 
    if request.method == 'POST':
        #red from data filled by user
        submitter = request.form["submitter"]
        fact = request.form["fact"]
        #persist to db
        new_fact = models.Fact(submitter=submitter,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    #Code for Get Route
    results = models.Fact.query.all()

    return render_template('facts/index.html', facts=results)