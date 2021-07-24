from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


# approutes go here
@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('dojo.html', dojos=dojos)

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def display_ninjas(id):
    data = {'id': id}
    dojos = Dojo.get_dojo_id(data)
    ninjas = Ninja.get_all_ninjas(data)
    return render_template('dojo_rost.html', ninjas=ninjas, dojos=dojos)