#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/caosornot/GitReto/Reto2ActuadoresSensores/Flask")

from Flask import app as application
application.secret_key = 'Add your secret key'
