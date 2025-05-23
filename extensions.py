# Este archivo nos ayudara a crear las importaciones circulares

from flask_sqlalchemy import SQLAlchemy

# Creamos un objeto de tipo SQLAlchemy que va controlar toda la base de datos
db = SQLAlchemy()