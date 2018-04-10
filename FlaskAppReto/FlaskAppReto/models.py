from datetime import datetime       #Importar funcion para obtener hora
from FlaskAppReto import db         #Importar BD

class RegTemp(db.Model):                            #Definición de estructura de base de datos
    id = db.Column(db.Integer, primary_key=True)    #Definir ID como llave primaria, es unica e incrementa sola
    temp = db.Column(db.String(10), index=True)     #Definir temp para guardar variable temperatura del JSON
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #Definir estampa de tiempo, si no se ingresa se toma por defecto la hora actual
