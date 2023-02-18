from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/')
def index():
    return redirect('/dojo')


@app.route('/dojo')
def dojo():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojo.html", all_dojos = all_dojos)

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_dojo(id)
    ninjas = Ninja.get_ninja_with_dojo()
    return render_template("show_dojo.html", dojo=dojo, ninjas=ninjas)

@app.route('/add_dojo', methods = ['POST'])
def add_dojo():
    dojo = Dojo.create_dojo(request.form)
    return redirect('/dojo')