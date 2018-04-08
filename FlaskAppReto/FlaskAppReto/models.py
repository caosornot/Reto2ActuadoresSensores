from datetime import datetime
from FlaskAppReto import db

class RegTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(10), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Temperatura: {}>'.format(self.temp)
