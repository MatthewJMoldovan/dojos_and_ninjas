from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    ninja = Ninja.create_ninja(request.form)
    return redirect(f'/show_dojo/{request.form["dojo_id"]}')