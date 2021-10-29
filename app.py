import re
from flask import Flask, render_template, request, flash, redirect
from flask_bcrypt import Bcrypt
from app2 import habitacion
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

# Ruta gestion usuarios + Listar usuarios
@app.route('/gestion_usuarios', methods=["GET","POST"])
def gestion_usuarios():
    lista_usuarios = list(Usuario.select())
    return render_template("/gestion_user.html", lista_usuarios=lista_usuarios)

# Ruta gestion huespedes
@app.route('/gestion_huespedes')
def gestion_huespedes():
    return render_template("/gestion_huespedes.html")

# Ruta gestion habitaciones + Listar habitaciones
@app.route('/gestion_habitaciones', methods=["GET","POST"])
def gestion_habitaciones():
    lista_habitaciones = list(Habitacion.select())

    return render_template("/gestion_hab.html", lista_habitaciones=lista_habitaciones)

# Ruta gestion reservas
@app.route('/gestion_reservas')
def gestion_reservas():
    return render_template("/gestion_reservas.html")

# Ruta gestion comentarios
@app.route('/gestion_comentarios')
def gestion_comentarios():
    return render_template("/gestion_comentarios.html")

# ----------------------------------------------
# FUNCIONES DE LA APLICACION
# ----------------------------------------------

# Crear habitaciones
@app.route('/gestion_habitaciones/save', methods=["POST"])
def gestion_habitaciones_save():
    id_hab = request.form["id_habitacion"]
    tipo_hab = int(request.form["tipo_habitacion"])
    cant_personas = request.form["cant_huespedes"]
    precio_hab = request.form["precio_habitacion"]
    estado_hab = request.form["status_habitacion"]

    habitacion, creado = Habitacion.get_or_create(id=id_hab, precio=precio_hab, tipo_habitacion=tipo_hab, cant_personas=cant_personas, estado=estado_hab, deleted=1)

    return redirect("/gestion_habitaciones")

# Editar habitaciones
@app.route('/gestion_habitaciones/update', methods=["POST"])
def gestion_habitaciones_update():
    id_hab = request.form["id_habitacion_e"]
    tipo_hab = int(request.form["tipo_habitacion_e"])
    cant_personas = request.form["cant_huespedes_e"]
    precio_hab = request.form["precio_habitacion_e"]
    estado_hab = int(request.form["status_habitacion_e"])

    habitacion = list(Habitacion.select().where(Habitacion.id==id_hab))

    habitacion[0].tipo_habitacion = str(tipo_hab)
    habitacion[0].cant_personas = cant_personas
    habitacion[0].precio = precio_hab
    habitacion[0].estado = estado_hab

    return redirect("/gestion_habitaciones")

# Crear Usuarios
@app.route('/gestion_usuarios/save', methods=["GET","POST"])
def gestion_usuarios_save():
    username = request.form["username"]
    password = request.form["password"]
    nombre = request.form["id_nombre"]
    apellido = request.form["id_apellido"]
    tipo_usuario = int(request.form["tipo_usuario"])
    estado = int(request.form["estado"])

    usuario, creado = Usuario.get_or_create(username =username, password=bcrypt.generate_password_hash(password), nombre=nombre, apellido=apellido, tipo_usuario=tipo_usuario, deleted=estado)


    return redirect("/gestion_usuarios")


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