from flask import Flask, render_template, request, flash, redirect
from models import *
from config import dev

app= Flask(__name__)


# app.secret_key = os.urandom(24)
app.config.from_object(dev)
db.init_app(app)

habitaciones = [('Individual', 'Una habitación asignada a una persona. Puede tener una o más camas.', '1', 'off'), 
                ('Doble', 'Una habitación asignada a dos personas. Puede tener una o más camas.', '2', 'off'), 
                ('Triple', 'Una habitación asignada a tres personas. Puede tener dos o más camas.', '3', 'off')]

usuarios = [("Sandra Patricia", "Mangas Galvan", "smangas", 'off'),
                 ("Diego Andres", "Gutierrez Blanco", "dmartinez", 'off'),
                 ("Angel Santiago", "Jimenez Vargas", "ajimenez", 'off')]                                                                                        

sesion_iniciada = False

@app.route('/')
def login():
    global sesion_iniciada
    if request.method == "GET":
        return render_template("login.html")
    else:
        sesion_iniciada = True    
        return redirect('/home') 
  
@app.route("/home/mision_vision")
def mision_vision():
    return render_template("home/mision_vision.html")

@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.method=='POST':
        userid = request.form['usuario']
        password = request.form['password']
        if userid =="superadmin":
            return render_template('HomeSuperAdmin.html', usuario=userid)
        elif userid == "admin":
            return render_template('HomeAdmin.html', usuario=userid, clave=password)
        elif userid == "cliente":
            return render_template('HomeCliente.html', usuario=userid, clave=password)
        else :
            return render_template('login.html')
    else :
        return render_template('login.html',       
       sesion_iniciada=sesion_iniciada,
       habitaciones=habitaciones
    )

@app.route("/login", methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    if request.method == "GET":
        return render_template("login.html")
    else:
        sesion_iniciada = True    
        return redirect('/home')  

@app.route("/perfil", methods=["GET","POST"])#En construcción
def perfil():
     return "Página perfil de usuario"

@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/home')                

@app.route('/registrarhabitaciones', methods=['GET', 'POST'])
def registrar_habitaciones():
    if request.method == 'POST':
        tipo_habitacion = request.form['tipo_habitacion']
        detalle_habitacion = request.form['detalle_habitacion']
        valoracion = request.form['valoracion']
        check = request.form['check']
        habitacion = []
        habitacion = (tipo_habitacion,detalle_habitacion,valoracion,check)
        global habitaciones
        habitaciones.append(habitacion)
        print(habitaciones)
        flash('Registro Exitoso', 'success')
        return render_template('habitacion.html')
    else :
        flash('Por favor ingresa una habitacion', 'success')
        return render_template('habitacion.html')

@app.route('/editarhabitacion/<id_habitacion>', methods=['GET','POST'])
def editar_habitaciones(id_habitacion):
    if request.method == 'POST':
        tipo_habitacion = request.form['tipo_habitacion']
        detalle_habitacion = request.form['detalle_habitacion']
        valoracion = request.form['valoracion']
        check = request.form['check']
        idhab = request.form['idHabitacion']#idm
        habitacion = []
        habitacion = (tipo_habitacion,detalle_habitacion,valoracion,check)
        global habitaciones
        index = int(idhab)
        habitaciones[index] = (habitacion)
        print(habitaciones)
        flash('Actualizacion Exitosa', 'error')
        return redirect('/listar_habitaciones')
    else:
      id_habitacion = int(id_habitacion)
      return render_template('editarhabitacion.html', id_habitacion = id_habitacion, habitacion = habitaciones[id_habitacion])

@app.route('/eliminarhabitacion/<id_habitacion>', methods=['GET'])
def eliminar_habitacion(id_habitacion):
    global habitacion
    idhab = int(id_habitacion)
    print(idhab)
    print(habitaciones)
    if(len(habitaciones) > (idhab)):
      habitaciones.pop(idhab)
      flash('Eliminado con éxito')
      return redirect('/listar_habitaciones')
    else:
      flash('No se pudo eliminar')
      return redirect('/listar_habitaciones')

@app.route('/listar_habitaciones', methods=['GET'])
def listaHabitaciones():
  print(habitaciones)
  return render_template('listarhabitaciones.html', habitaciones=habitaciones)

#Reserva de habitación en construcción  
@app.route("/reserva_habitacion/habitacion/<id_habitacion>", methods=["GET","POST"])
def detalle_reserva(id_habitacion):
    try:
        id_habitacion = int(id_habitacion)
    except Exception as e:  
        id_habitacion = 0

    if habitacion in habitaciones:
       return habitaciones[id_habitacion]
    else:
        return f"La habitación: ({id_habitacion}) no esta disponible"

#Usuarios
@app.route('/registrarusuarios', methods=['GET', 'POST'])
def registrar_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        nusuario = request.form['nusuario']
        check = request.form['check']
        usuario = []
        usuario = (nombre,apellido,nusuario,check)
        global usuarios
        usuarios.append(usuario)
        print(usuarios)
        flash('Registro Exitoso', 'success')
        return render_template('usuario.html')
    else :
        flash('Por favor ingresa un usuario', 'success')
        return render_template('usuario.html')

@app.route('/editarusuario/<id_usuario>', methods=['GET','POST'])
def editar_usuarios(id_usuario):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        nusuario = request.form['nusuario']
        check = request.form['check']
        userid = request.form['idUsuario']
        usuario = []
        usuario = (nombre,apellido,nusuario,check)
        global usuarios
        index = int(userid)
        usuarios[index] = (usuario)
        print(usuarios)
        flash('Actualizacion Exitosa', 'error')
        return redirect('/listar_usuarios')
    else:
      id_usuario = int(id_usuario)
      return render_template('editarusuario.html', id_usuario = id_usuario, usuario = usuarios[id_usuario])
        
@app.route('/eliminarusuario/<id_usuario>', methods=['GET'])
def eliminar_usuario(id_usuario):
    global usuarios
    userid = int(id_usuario)
    print(userid)
    print(usuarios)
    if(len(usuarios) > (userid)):
      usuarios.pop(userid)
      flash('Eliminado con éxito')
      return redirect('/listar_usuarios')
    else:
      flash('No se pudo eliminar')
      return redirect('/listar_usuarios')

@app.route('/listar_usuarios', methods=['GET'])
def listaUsuarios():
  print(usuarios)
  return render_template('listarusuarios.html', usuarios=usuarios)

@app.route("/calificar_habitación/<id_habitacion>", methods=["GET, POST"])
def habitacion(id_habitacion):
    return f"Mostrar calificación: {id_habitacion}"

'''

@app.route("/comentarios/usuario/<id_usuario>", methods=["GET, POST"])
def ingreso(usuario):
    return f"Mostrar comentarios: {comentario}"  

@app.route('"usuario/<id_usuario>/dashboard",methods=["GET","POST"])
def panel_admin(usuario):
    return render("panel_admin.html")


@app.route("/usuario/<id_usuario>/dashboard/GesHabitacion",methods=["GET","POST"])
def panel_admin(usuario):
    return render("gestion_habitaciones.html")    

'''

if __name__=='__main__':
    app.run()