import datetime
from app import *
from playhouse.shortcuts import model_to_dict

@app.cli.command("crear_datos_iniciales")
def crear_datos_iniciales():
  db.init_app(app)

  # Usuarios de ejemplo
  u1 = Usuario.get_or_create(username ="siadoa", password="123456", nombre="Andres", apellido="Henriquez", tipo_usuario=0, deleted=1)
  u2 = Usuario.get_or_create(username ="dmartinez", password="123456", nombre="Diego", apellido="Gutierrez", tipo_usuario=1, deleted=1)
  u3 = Usuario.get_or_create(username ="smangas", password="123456", nombre="Sandra", apellido="Mangas", tipo_usuario=2, deleted=1)
  u4 = Usuario.get_or_create(username ="ajimenez", password="123456", nombre="Angel", apellido="Jimenez", tipo_usuario=2, deleted=1)

  # Clientes de ejemplo
  # c1 = Cliente.get_or_create(usuario=u3, telefono="312547896", email="smangas@uninorte.edu.co", direccion="Calle 123434")
  # c1 = Cliente.get_or_create(usuario=u4, telefono="300458796", email="ajimenez@uninorte.edu.co", direccion="Carrera 123434")

  # Habitaciones de ejemplo
  h1 = Habitacion.get_or_create(id="101", precio=100, tipo_habitacion=0, cant_personas=2, estado=1, deleted=1)
  h2 = Habitacion.get_or_create(id="201", precio=250, tipo_habitacion=2, cant_personas=4, estado=1, deleted=1)
  h3 = Habitacion.get_or_create(id="301", precio=300, tipo_habitacion=3, cant_personas=2, estado=1, deleted=1)
  h4 = Habitacion.get_or_create(id="401", precio=200, tipo_habitacion=1, cant_personas=1, estado=1, deleted=1)

  # Calificaciones de ejemplo
  # cal1 = Calificacion.get_or_create(habitacion=h1, cliente=u3, comentario="Exelente habitacion", calificacion=5)
  # cal2 = Calificacion.get_or_create(habitacion=h2, cliente=u3, comentario="Otro comentario", calificacion=4)
  # cal3 = Calificacion.get_or_create(habitacion=h1, cliente=u4, comentario="Mala habitacion", calificacion=2)

  # Reservas de ejemplo
  # r1 = Reserva.get_or_create(habitacion=h4, usuario=u1, fecha_ingreso=datetime.datetime(2021, 6, 1), fecha_salida=datetime.datetime(2021, 6, 5), cant_personas=1, deleted=1)
  # r2 = Reserva.get_or_create(habitacion=h3, usuario=u3, fecha_ingreso=datetime.datetime(2021, 8, 15), fecha_salida=datetime.datetime(2021, 8, 20), cant_personas=2, deleted=1)
  # r3 = Reserva.get_or_create(habitacion=h2, usuario=u1, fecha_ingreso=datetime.datetime(2021, 9, 18), fecha_salida=datetime.datetime(2021, 9, 23), cant_personas=3, deleted=1)

  buscar = list(Usuario.select().where(Usuario.username=="siadoa"))

  print(buscar[0].password)
  print(model_to_dict(buscar[0]))

app.cli()