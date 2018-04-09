from flask import render_template, jsonify, request
from FlaskAppReto import app, db
from FlaskAppReto.models import RegTemp

@app.route("/")
def index():
    return render_template('template.html')

@app.route("/temperatura")
def historico():
    return render_template('temperatura.html')

@app.route("/implementacion")
def implementacion():
    return render_template('implementacion.html')

@app.route("/temperatura/add_entry", methods=['POST'])
def add_entry():
    print("p1")
    content = request.get_json()
    tempC = content.get('temp')
    print (tempC)
    u = RegTemp(temp = tempC)
    print ("p3")
    db.session.add(u)
    print ("p4")
    db.session.commit()
    print("p5")
    reponse_content='OK'
    return jsonify(content)
