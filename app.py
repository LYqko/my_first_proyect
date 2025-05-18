#Flask is the library that helps to create a server for the API

from flask import Flask, render_template, request, redirect, url_for

# Desde el archivo routes quiero que importes la función "cargar_rutas"
from routes import cargar_rutas

from flask_sqlalchemy import SQLAlchemy

# flask: Library
# Flask: class

# I create a object that has a meths for a server.
app = Flask(__name__)

# 1. Configuramos la app para conectarse a una db
app.config['SQLALCHEMY_DATABASE_URI'] = ''

# 2. Desactivamos el seguimiento de modificaciones
app.config['SQLALCHEMI_TRACK-MODIFICATIONS  '] = False



cargar_rutas(app)

app.run(port=8526)


# el método run le va indicar a nuestro servdor que va comenzar 
# a recirbr peticiones (servir)
# puero: 8080: le indica al usuario que accederá al servidor que creamos
# puerto 22: Este puerto usa http para enviar información
# puerto 23: Telnet
# puerto 443: Este puerto usa https para enviar información
# etc. 

