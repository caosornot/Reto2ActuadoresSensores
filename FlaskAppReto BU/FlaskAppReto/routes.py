from flask import render_template
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
    print("p0")
    request_json     = request.get_json()
    tempC            = request_json.get('temp')
    response_content = 'None'

    if tempC is not None and value2 is not None:
        print("p3")
    	u = RegTemp(temp = tempC)
    	db.session.add(u)
    	db.session.commit()
        response_content = conn.commit()

    return jsonify(response_content)

