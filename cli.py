import datetime
from app import *
from playhouse.shortcuts import model_to_dict

@app.cli.command("crear_datos_iniciales")
def crear_datos_iniciales():
  bcrypt = Bcrypt(app)
  db.init_app(app)

  # Usuarios de ejemplo
  u1, creado = Usuario.get_or_create(username ="siadoa", password="123456", nombre="Andres", apellido="Henriquez", tipo_usuario=0, deleted=1)
  u2, creado = Usuario.get_or_create(username ="dmartinez", password="123456", nombre="Diego", apellido="Gutierrez", tipo_usuario=1, deleted=1)
  u3, creado = Usuario.get_or_create(username ="smangas", password="123456", nombre="Sandra", apellido="Mangas", tipo_usuario=2, deleted=1)
  u4, creado = Usuario.get_or_create(username ="ajimenez", password="123456", nombre="Angel", apellido="Jimenez", tipo_usuario=2, deleted=1)
  # u5, creado = Usuario.get_or_create(username ="test1", password=bcrypt.generate_password_hash("123456"), nombre="Test", apellido="Test", tipo_usuario=0, deleted=1)

  # Clientes de ejemplo
  c1, creado = Cliente.get_or_create(usuario=u3, telefono="312547896", email="smangas@uninorte.edu.co", direccion="Calle 123434")
  c1, creado = Cliente.get_or_create(usuario=u4, telefono="300458796", email="ajimenez@uninorte.edu.co", direccion="Carrera 123434")

  # Habitaciones de ejemplo
  h1, creado = Habitacion.get_or_create(id="101", precio=100, tipo_habitacion=0, cant_personas=2, estado=1, deleted=1)
  h2, creado = Habitacion.get_or_create(id="201", precio=250, tipo_habitacion=2, cant_personas=4, estado=1, deleted=1)
  h3, creado = Habitacion.get_or_create(id="301", precio=300, tipo_habitacion=3, cant_personas=2, estado=1, deleted=1)
  h4, creado = Habitacion.get_or_create(id="401", precio=200, tipo_habitacion=1, cant_personas=1, estado=1, deleted=1)

  # Calificaciones de ejemplo
  cal1, creado = Calificacion.get_or_create(habitacion=h1, cliente=u3, comentario="Exelente habitacion", calificacion=5)
  cal2, creado = Calificacion.get_or_create(habitacion=h2, cliente=u3, comentario="Otro comentario", calificacion=4)
  cal3, creado = Calificacion.get_or_create(habitacion=h1, cliente=u4, comentario="Mala habitacion", calificacion=2)

  # Reservas de ejemplo
  r1, creado = Reserva.get_or_create(habitacion=h4, usuario=u1, fecha_ingreso=datetime.datetime(2021, 6, 1), fecha_salida=datetime.datetime(2021, 6, 5), cant_personas=1, deleted=1)
  r2, creado = Reserva.get_or_create(habitacion=h3, usuario=u3, fecha_ingreso=datetime.datetime(2021, 8, 15), fecha_salida=datetime.datetime(2021, 8, 20), cant_personas=2, deleted=1)
  r3, creado = Reserva.get_or_create(habitacion=h2, usuario=u1, fecha_ingreso=datetime.datetime(2021, 9, 18), fecha_salida=datetime.datetime(2021, 9, 23), cant_personas=3, deleted=1)

  buscar = list(Usuario.select().where(Usuario.username=="siadoa"))

  print(buscar[0].tipo_usuario)
  print(model_to_dict(buscar[0]))

app.cli()