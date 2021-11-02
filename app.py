from flask import Flask, render_template, request, flash, redirect
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from datetime import datetime
from config import dev
from models import *

app= Flask(__name__)
app.config.from_object(dev)
login_manager = LoginManager()
bcrypt = Bcrypt(app)
db.init_app(app)
login_manager.init_app(app)

# RUTAS DE LA APLICACION - VISTAS CLIENTE

login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return Usuario.get(user_id)

# Ruta Login
@app.route("/login", methods=["GET","POST"])
def login():
    username = request.form["usuario"]
    password = request.form["password"]

    if request.method == "GET":
        return render_template("login.html")
    else:
        return redirect('/home')

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

# Ruta registro
@app.route('/registro')
def registro():
    return render_template("/registro.html")

# -------------------------------------
# RUTAS DE LA APLICACION - VISTAS ADMIN
# -------------------------------------

# Ruta inicio admin - Ruta temporal
@app.route('/admin')
def inicioAdmin():
    return render_template("/inicio_admin.html")

# Ruta gestion usuarios + Listar usuarios
@app.route('/gestion_usuarios', methods=["GET","POST"])
def gestion_usuarios():
    tipo_usuario = "Traer el rol de usuario"
    lista_usuarios = list(Usuario.select().where(Usuario.deleted==False))

    return render_template("/gestion_user.html", lista_usuarios=lista_usuarios) #rol=tipo_usuario

# Ruta gestion huespedes + Listar huespedes
@app.route('/gestion_huespedes')
def gestion_huespedes():
    tipo_usuario = "Traer el rol de usuario"
    lista_huespedes = list(Cliente.select(Cliente, Usuario).join(Usuario).where(Usuario.deleted==False))

    return render_template("/gestion_huespedes.html", lista_huespedes=lista_huespedes) #rol=tipo_usuario

# Ruta gestion habitaciones + Listar habitaciones
@app.route('/gestion_habitaciones', methods=["GET","POST"])
def gestion_habitaciones():
    tipo_usuario = "Traer el rol de usuario"
    lista_habitaciones = list(Habitacion.select().where(Habitacion.deleted==False))

    return render_template("/gestion_hab.html", lista_habitaciones=lista_habitaciones) #rol=tipo_usuario

# Ruta gestion reservas + Listar reservas
@app.route('/gestion_reservas')
def gestion_reservas():
    lista_reservas = list(Reserva.select().where(Reserva.deleted==False))

    return render_template("/gestion_reservas.html", lista_reservas=lista_reservas)

# Ruta gestion comentarios
@app.route('/gestion_comentarios')
def gestion_comentarios():
    id_hab = "101"
    username = "adcastaneda"
    if id_hab:
        habitacion = list(Habitacion.select().where(Habitacion.id==id_hab & Habitacion.deleted==False))[0]
        lista_comentarios = habitacion.calificaciones
        
    
    return render_template("/gestion_comentarios.html", lista_comentarios=lista_comentarios)

# Ruta graficas
@app.route('/graficas')
def graficas():
    return render_template("/graficas.html")

# ----------------------------------------------
# FUNCIONES DE LA APLICACION - DASHBOARD
# ----------------------------------------------

# Crear habitaciones
@app.route('/gestion_habitaciones/save', methods=["POST"])
def gestion_habitaciones_save():
    id_hab = request.form["id_habitacion"]
    tipo_hab = int(request.form["tipo_habitacion"])
    cant_personas = request.form["cant_huespedes"]
    precio_hab = request.form["precio_habitacion"]
    estado_hab = request.form["status_habitacion"]

    habitacion, creado = Habitacion.get_or_create(id=id_hab, precio=precio_hab, tipo_habitacion=tipo_hab, cant_personas=cant_personas, estado=estado_hab, deleted=False)

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

    usuario, creado = Usuario.get_or_create(username =username, password=bcrypt.generate_password_hash(password), nombre=nombre, apellido=apellido, tipo_usuario=tipo_usuario, estado=estado, deleted=False)

    return redirect("/gestion_usuarios")

# Crear huespedes
@app.route('/gestion_huespedes/save', methods=["GET","POST"])
def gestion_huespedes_save():
    username = request.form["username"]
    password = request.form["password"]
    nombre = request.form["nombre_usuario"]
    apellido = request.form["apellido_usuario"]
    telefono = request.form["telefono_usuario"]
    email = request.form["email_usuario"]
    direccion = request.form["direccion_usuario"]
    tipo_usuario = 2
    estado = int(request.form["status_usuario"])

    usuario, creado = Usuario.get_or_create(username =username, password=bcrypt.generate_password_hash(password), nombre=nombre, apellido=apellido, tipo_usuario=tipo_usuario, estado=estado, deleted=False)

    cliente, creado = Cliente.get_or_create(usuario=usuario, telefono=telefono, email=email, direccion=direccion)

    return redirect("/gestion_huespedes")

# Crear Reservas
@app.route('/gestion_reservas/save', methods=["GET","POST"])
def gestion_reservas_save():
    # Traer el username del usuario que registra
    username = "admin1" #Viene del login
    nombre = request.form["nombre_usuario"]
    apellido = request.form["apellido_usuario"]
    telefono = request.form["telefono_usuario"]
    email = request.form["email_usuario"]
    direccion = request.form["direccion_usuario"]
    tipo_hab = int(request.form["tipo_habitacion"])
    fecha_llegada = request.form["check_in"].split("/")
    fecha_salida = request.form["check_out"].split("/")
    cant_personas = int(request.form["cant_huespedes"])
    estado = int(request.form["estado_reserva"])
    
    habitacion = list(Habitacion.select().where(Habitacion.tipo_habitacion==tipo_hab & Habitacion.estado==1))[0]

    reserva, creado = Reserva.get_or_create(habitacion=habitacion, usuario=username, nombre_cliente=nombre, apellido_cliente=apellido, telefono_cliente=telefono, email_cliente=email, direccion_cliente=direccion, fecha_ingreso=datetime(int(fecha_llegada[0]), int(fecha_llegada[1]), int(fecha_llegada[2])), fecha_salida=datetime(int(fecha_salida[0]), int(fecha_salida[1]), int(fecha_salida[2])), cant_personas=cant_personas, estado=estado,deleted=False)

# Editar usuarios

# Editar huespedes

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

# Editar reservas

# Editar comentarios

# Eliminar 

# ----------------------------------------------
# FUNCIONES DE LA APLICACION - PAGINA CLIENTE
# ----------------------------------------------

# Registrar usuario
@app.route('/registrarusuarios', methods=['POST', 'GET'] )
def registrar_usuarios():

    nombre = request.form["nombre_usuario"]
    apellido = request.form["apellido_usuario"]
    usuario = request.form["usuario"]
    email = request.form["email"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    password = request.form["contrasena"]
    confirm_pass = request.form["contrasena2"]
    
    # if password == confirm_pass: 
    usuario, creado = Usuario.get_or_create(username =usuario, password=bcrypt.generate_password_hash(password), nombre=nombre, apellido=apellido, tipo_usuario=2, estado=1, deleted=False)

    cliente, creado = Cliente.get_or_create(usuario=usuario, telefono=telefono, email=email, direccion=direccion)

    return redirect('/')

# Crear reserva
@app.route('/crear_reserva', methods=['POST', 'GET'] )
def crear_reserva():
    # Traer el username del cliente
    username = "dfernandez" #Viene del login
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    email = request.form["email"]
    tipo_hab = int(request.form["tipo_hab"])
    fecha_llegada = request.form["check_in"][slice(10)].split("-")
    fecha_salida = request.form["check_out"][slice(10)].split("-")
    cant_adultos = int(request.form["cant_ad"])
    cant_ninos = int(request.form["cant_ni"])
    cant_personas = cant_ninos + cant_adultos

    habitacion = list(Habitacion.select().where(Habitacion.tipo_habitacion==tipo_hab & Habitacion.estado==1))[0]

    reserva, creado = Reserva.get_or_create(habitacion=habitacion, usuario=username, nombre_cliente=nombre, apellido_cliente=apellido, telefono_cliente=telefono, email_cliente=email, direccion_cliente=direccion, fecha_ingreso=datetime(int(fecha_llegada[0]), int(fecha_llegada[1]), int(fecha_llegada[2])), fecha_salida=datetime(int(fecha_salida[0]), int(fecha_salida[1]), int(fecha_salida[2])), cant_personas=cant_personas, estado=2,deleted=False)

    return redirect("/reserva")

# Editar reserva

# Editar perfil usuario


if __name__=='__main__':
    app.run()