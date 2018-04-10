# ACTUADORES Y SENSORES - RETO 2
# Carlos Andres Osorno Tejada
# Archivo routes.py donde creo las paginas de la aplicacion y les doy funcion y direccionamiento

from flask import render_template, jsonify, request #se importa funciones de render_template para paginas html, jsonify y request para procesar los POST
from FlaskAppReto import app, db                    #Se importa App de Flask y Base de Datos db
from FlaskAppReto.models import RegTemp             #Del archivo models.py se importa la class RegTemp la cual contiene la estructura de la BD

@app.route("/")                                 #Creación de pagina web raiz
def index():
    return render_template('template.html')     #Renderiza la pagina templatee.html de la carpeta templates

@app.route("/temperatura")                      #Ruta de temperatura
def temperatura():
    return render_template('temperatura.html',items=RegTemp.query.all())    #Renderiza la pagina temperatura.html con items  = info basedatos

@app.route("/implementacion")                   #Ruta de Implementación donde se habla de paginas y tutoriales usados
def implementacion():
    return render_template('implementacion.html')

@app.route("/temperatura/add_entry", methods=['POST'])  #Ruta para recibir datos de temperatura METHOD POST
def add_entry():
    content = request.get_json()    #Se lee contenido JSON recibido
    tempC = content.get('temp')     #Se extrae variable temp del JSON
    u = RegTemp(temp = tempC)       #Se crea variable con formato de BD
    db.session.add(u)               #Se Adiciona el cambio en la BD
    db.session.commit()             #Se registran lso cambios en la BD
    
    return 'OK'
