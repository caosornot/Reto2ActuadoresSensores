# ACTUADORES Y SENSORES - RETO 2
# Carlos Andres Osorno Tejada
# Archivo __init__.py para marcar directorio como paquete de python

from flask import Flask #Importar FLASK
from config import Config   #Importar archivo funcion Config del archivo config
from flask_sqlalchemy import SQLAlchemy #Importar libreria para base de datos
from flask_migrate import Migrate   #Importar libreria para migrar base de datos en caso de cambios

app = Flask(__name__)   #Inicializa función app
app.config.from_object(Config)   #Se carga configuración de archivo Config en la aplicacion flask
db = SQLAlchemy(app)            #Se inicia la base de datos y se guarda en db para representar la base de Datos
migrate = Migrate(app, db)      #Se crea el motor de migracion

from FlaskAppReto import routes, models  #Se importa los archivo routes.py y models.py
