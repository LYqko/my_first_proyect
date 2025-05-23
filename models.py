# SQL - Querys 


from extensions import db
# Vamos a crear un modelo 
# Vamos a crear un modelo que es un plano de como se ve la tabla en sql

# Modulo para hashear las contraseñas
from werkzeug.security import generate_password_hash, check_password_hash

# generate_password_hash: recbe un textio y  lo hashea en una serie de caracteres con longitud igual en todos casos
# check_password_hash: recibe un texto y lo compara con el hash que se le pasa como segundo argumento
class Usuario(db.Model):
    # 1. Nombre de la tabla
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def hashear_password(self,password_original):
      self.password = generate_password_hash(password_original)

    def verificar_password(self, password_plano):
      # Comparamos el password plano con el hash
      return check_password_hash(self.password, password_plano)

# Creamos una conexión a la base de datos para agregar información
    def save(self):
      db.session.add(self)

    # Nos aseguramos de que los cambios se hagan
      db.session.commit()

    def delete(self):
      db.session.delete(self)

    # Nos aseguramos de que los cambios se hagan
      db.session.commit()