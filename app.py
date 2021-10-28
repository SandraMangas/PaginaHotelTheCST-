from flask import Flask, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from config import dev
from models import *

app= Flask(__name__)
app.config.from_object(dev)
bcrypt = Bcrypt(app)
db.init_app(app)                                                                              

sesion_iniciada = False

# RUTAS DE LA APLICACION - VISTAS CLIENTE

# Ruta principal
@app.route('/')
def inicio():
    return render_template("/inicio.html")

# Ruta nosotros
@app.route('/nosotros')
def nosotros():
    return render_template("/nosotros.html")

# Ruta reserva
@app.route('/reserva')
def reserva():
    return render_template("/habitaciones_disponibles.html")

# Ruta galeria
@app.route('/galeria')
def galeria():
    return render_template("/galeria.html")

# Ruta contacto
@app.route('/contacto')
def contacto():
    return render_template("/contacto.html")

# Ruta Login
@app.route("/login", methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    if request.method == "GET":
        return render_template("login.html")
    else:
        sesion_iniciada = True
        return redirect('/home')

# Ruta registro
@app.route('/registro')
def registro():
    return render_template("/registro.html")

# RUTAS DE LA APLICACION - VISTAS ADMIN

# Ruta inicio admin
@app.route('/admin')
def inicioAdmin():
    return render_template("/inicio_admin.html")

# Ruta gestion usuarios
@app.route('/gestion_usuarios')
def gestion_usuarios():
    return render_template("/gestion_user.html")

# Ruta gestion huespedes
@app.route('/gestion_huespedes')
def gestion_huespedes():
    return render_template("/gestion_huespedes.html")

# Ruta gestion habitaciones
@app.route('/gestion_habitaciones')
def gestion_habitaciones():
    return render_template("/gestion_hab.html")

# Ruta gestion reservas
@app.route('/gestion_reservas')
def gestion_reservas():
    return render_template("/gestion_reservas.html")

# Ruta gestion comentarios
@app.route('/gestion_comentarios')
def gestion_comentarios():
    return render_template("/gestion_comentarios.html")

# FUNCIONES DE LA APLICACION

# Registrar usuario
@app.route('/registrarusuarios', methods=['POST', 'GET'] )
def registrar_usuarios():

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        usuario = request.form['usuario']
        #usuario = []
        #usuario = (nombre,apellido,nusuario,check)
        #global usuarios
        #usuarios.append(usuario)
        #print(usuarios)
        #flash('Registro Exitoso', 'success')
        #return render_template('usuario.html')
    #else :
        #flash('Por favor ingresa un usuario', 'success')
        return render_template('inicio.html')


if __name__=='__main__':
    app.run()