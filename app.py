from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request
#import os
#import sqlite3


app = Flask(__name__)
#app.secret_key = os.urandom(20)

lista_usuarios = ["smangas", "arodriguez", "cvazquez", "dmartinez"]
hab_disponibles = {
    101:  {'titulo': "Individual", 'cuerpo':"una habitación asignada a una persona. Puede tener una o más camas.",'imagenes':['img 1', 'img 2' ]},
    102:  {'titulo': "Doble", 'cuerpo':"Una habitación asignada a dos personas. Puede tener una o más camas.", 'imagenes':['img 1', 'img 2' ]},
    202:  {'titulo': "Triple", 'cuerpo':"Una habitación asignada a tres personas. Puede tener dos o más camas.",'imagenes':['img 1', 'img 2' ]},
    302:  {'titulo': "Quad", 'cuerpo':"Una sala asignada a cuatro personas. Puede tener dos o más camas.",'imagenes':["img 1", 'img 2' ]},
    402:  {'titulo':"Queen", 'cuerpo':"Una habitación con una cama de matrimonio. Puede ser ocupado por una o más personas.", 'imagenes':['img 1', 'img 2' ]},
    501:  {'titulo':"Estudio", 'cuerpo':"Una habitación con una cama de estudio, un sofá que se puede convertir en una cama. También puede tener una cama adicional.", 'imagenes':['img 1', 'img 2' ]}
}

sesion_iniciada = False

@app.route("/", methods =["GET"])
@app.route("/inicio", methods=["GET"])
def inicio():
   # Si ya inició sesión -> Lista de habitaciones disponibles
   # Sino Bienvenida
    return render(
       "inicio.html",
       sesion_iniciada=sesion_iniciada,
       hab_disponibles=hab_disponibles
    )

@app.route("/registro", methods=["GET","POST"])
def registro():
    return "Página de registro"

@app.route("/ingreso", methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    if request.method == "GET":
        return render("ingreso.html")
    else:
        sesion_iniciada = True    
        return redirect('/inicio') 

@app.route("/salir", methods=["POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/inicio')      

@app.route("/perfil", methods=["GET","POST"])
def perfil():
     return "Página perfil de usuario"

#Buscar usuario dentro del perfil de administrador o superadministrador
@app.route("/usuario/<id_usuario>", methods=["GET"])
def usuario_info(id_usuario):
    if id_usuario in lista_usuarios:
        return f"Perfil de usuario:: {id_usuario}"
    else:    
        return f"Usuario: {id_usuario} no existe"

@app.route("/habitacion/<id_habitacion>", methods=["GET","POST"])
def detalle_habitacion(id_habitacion):
    try:
        id_habitacion = int(id_habitacion)
    except Exception as e:
        id_habitacion = 0    
        return f"Detalle habitación: {id_habitacion}"

@app.route("/reserva_habitacion/habitacion/<id_habitacion>", methods=["GET","POST"])
def detalle_reserva(id_habitacion):
    try:
        id_habitacion = int(id_habitacion)
    except Exception as e:  
        id_habitacion = 0

    if id_habitacion in hab_disponibles:
       return hab_disponibles[id_habitacion]
    else:
        return f"La habitación: ({id_habitacion}) no esta disponible"

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

if __name__=="__main__":
    app.run(debug=True)     


