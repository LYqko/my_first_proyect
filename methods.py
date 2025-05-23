from models import Usuario

# Necesitamos un metodo para que el usuario pueda registrarse 
def crear_cuenta(nombre, correo, password):

    usuario_existente = Usuario.query.filter_by(email=correo).first()

    # Revisamos si el lo que regresa esa query es diferente de None
    if usuario_existente is not None:
        print('El correo ya existe')
        return {'status': 'error', 'mensaje': 'El correo ya existe'}
    # Esto solo se ejecuta si en la db no existe la cuenta que el usuario.

    # 1. Creamos un objeto de tip usurio ue teddra informacio para la base de datos
    nuevo_usuario = Usuario(name=nombre, email=correo, password=password)

    nuevo_usuario.hashear_password(password_original=password)
    

    # Guardamos este nuevo objeto en la db
    nuevo_usuario.save()

    
    return {'status': 'ok', 'correp':correo}

def iniciar_sesion(coreo, password):

    # Variable que contenga usuarios filtrados a través de un parametroo
    usuarios_existente = Usuario.query.filter_by(email='correo').first()
    
    # Si el usuario existe entonces el usuario puede iniciar sesion
    # Si el usuario no existe entonces el usuario no puede iniciar sesion
    if usuarios_existente is not None:
        print('El usuario existe')
        return {'status': 'ok', 'mensaje': 'El usuario existe'}
    
    # Si la contraseña del formulario es la de la db
    if usuarios_existente.verificar_password(password_plano=password):
        print('El password es correcto')
        return {'status': 'ok', 'mensaje': 'El password es correcto'}

# minuto 39:00


