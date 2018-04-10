from flask import render_template, jsonify, request
from FlaskAppReto import app, db
from FlaskAppReto.models import RegTemp

@app.route("/")
def index():
    return render_template('template.html')

@app.route("/temperatura")
def historico():

    return render_template('temperatura.html',items=RegTemp.query.all())

@app.route("/implementacion")
def implementacion():
    return render_template('implementacion.html')

@app.route("/temperatura/add_entry", methods=['POST'])
def add_entry():
    content = request.get_json()
    tempC = content.get('temp')
    u = RegTemp(temp = tempC)
    db.session.add(u)
    db.session.commit()
    reponse_content='OK'

    return jsonify(content)
