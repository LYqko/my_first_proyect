# Este archivo va a almacenar unica y exclisivamentre rurtas de nuestro servidor

from flask import Flask, render_template, request, redirect, url_for

def cargar_rutas(app):
# Este bloque de código es la base para todas las rutas

    @app.route('/')
    def pagina():
        return render_template ("index.html")


    # This is another route
    @app.route("/login")
    def informacion_leo():
        return render_template("login.html")
        

    # This is another route
    @app.route("/signup")
    def datos():
        return render_template("signup.html")

    # Esta ruta va manejar la información
    # Este metodo solo funcionara el inicio de sesión
    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        correo = request.form.get("email")
        password = request.form.get("password")

        print(f'''
        Correo: {correo}
        Contraseña: {password}


    ''')
        return redirect(url_for('pagina'))


    @app.route('/datos_crear_cuenta', methods=['POST'])
    def obtener_datos_cuenta():
        nombre = request.form.get('name')
        correo = request.form.get('email')
        password = request.form.get('password')

        print(f'''
        nombre: {nombre}
        correo: {correo}  
        password: {password}  
    ''')
        # Interceptamos la información del SignUp del usuario
        return redirect(url_for('pagina'))