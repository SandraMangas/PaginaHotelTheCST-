from datetime import datetime
from app import *
from playhouse.shortcuts import model_to_dict

@app.cli.command("crear_datos_iniciales")
def crear_datos_iniciales():
  bcrypt = Bcrypt(app)
  db.init_app(app)

  # Usuarios de ejemplo
  u1, creado = Usuario.get_or_create(username ="siadoa", password=bcrypt.generate_password_hash("123456"), nombre="Andres", apellido="Henriquez", tipo_usuario=0, estado=1, deleted=False)
  u2, creado = Usuario.get_or_create(username ="smangas", password=bcrypt.generate_password_hash("123456"), nombre="Sandra", apellido="Mangas", tipo_usuario=1, estado=1, deleted=False)
  u3, creado = Usuario.get_or_create(username ="adcastaneda", password=bcrypt.generate_password_hash("123456"), nombre="Andrea", apellido="Romero", tipo_usuario=1, estado=1, deleted=False)
  u4, creado = Usuario.get_or_create(username ="ramurillo", password=bcrypt.generate_password_hash("123456"), nombre="Rafael", apellido="Murillo", tipo_usuario=1, estado=1, deleted=False)
  u5, creado = Usuario.get_or_create(username ="dmartinez", password=bcrypt.generate_password_hash("123456"), nombre="Diego", apellido="Gutierrez", tipo_usuario=2, estado=1, deleted=False)
  u6, creado = Usuario.get_or_create(username ="ajimenez", password=bcrypt.generate_password_hash("123456"), nombre="Angel", apellido="Jimenez", tipo_usuario=2, estado=1, deleted=False)

  # Clientes de ejemplo
  c1, creado = Cliente.get_or_create(usuario=u5, telefono="312547896", email="dmartinez@uninorte.edu.co", direccion="Calle 30 10-25")
  c1, creado = Cliente.get_or_create(usuario=u6, telefono="300458796", email="ajimenez@uninorte.edu.co", direccion="Carrera 15 25-02")

  # Habitaciones de ejemplo
  h1, creado = Habitacion.get_or_create(id="101", precio=150, tipo_habitacion=0, cant_personas=2, estado=1, deleted=False)
  h2, creado = Habitacion.get_or_create(id="201", precio=250, tipo_habitacion=2, cant_personas=4, estado=1, deleted=False)
  h3, creado = Habitacion.get_or_create(id="301", precio=750, tipo_habitacion=3, cant_personas=2, estado=1, deleted=False)
  h4, creado = Habitacion.get_or_create(id="401", precio=200, tipo_habitacion=1, cant_personas=1, estado=1, deleted=False)
  h5, creado = Habitacion.get_or_create(id="501", precio=200, tipo_habitacion=2, cant_personas=2, estado=2, deleted=False)
  h6, creado = Habitacion.get_or_create(id="601", precio=200, tipo_habitacion=2, cant_personas=4, estado=2, deleted=True)

  # Calificaciones de ejemplo
  cal1, creado = Calificacion.get_or_create(habitacion=h1, cliente=u5, comentario="Exelente habitacion", calificacion=5, deleted=False)
  cal2, creado = Calificacion.get_or_create(habitacion=h2, cliente=u6, comentario="Mejorar el servicio", calificacion=3, deleted=False)
  cal3, creado = Calificacion.get_or_create(habitacion=h1, cliente=u5, comentario="Mala habitacion", calificacion=2, deleted=False)

  # Reservas de ejemplo
  r1, creado = Reserva.get_or_create(habitacion=h4, usuario=u2, nombre_cliente="Andres", apellido_cliente="Martinez", telefono_cliente="300516978", email_cliente="amartinez@gmail.com", direccion_cliente="Carrera 45 16-80", fecha_ingreso=datetime(2021, 10, 11), fecha_salida=datetime(2021, 10, 15), cant_personas=1, estado=1,deleted=False)
  r2, creado = Reserva.get_or_create(habitacion=h3, usuario="ajimenez", nombre_cliente="Angel", apellido_cliente="Jimenez", telefono_cliente="300458796", email_cliente="ajimenez@uninorte.edu.co", direccion_cliente="Carrera 15 25-02", fecha_ingreso=datetime(2021, 9, 1), fecha_salida=datetime(2021, 9, 5), cant_personas=2, estado=0,deleted=False)
  r3, creado = Reserva.get_or_create(habitacion=h4, usuario="dmartinez", nombre_cliente="Diego", apellido_cliente="Gutierrez", telefono_cliente="312547896", email_cliente="dmartinez@uninorte.edu.co", direccion_cliente="Calle 30 10-25", fecha_ingreso=datetime(2021, 6, 20), fecha_salida=datetime(2021, 6, 25), cant_personas=1, estado=2,deleted=False)

  buscar = list(Usuario.select().where(Usuario.username=="siadoa"))

  print(buscar[0].tipo_usuario)
  print(model_to_dict(buscar[0]))

app.cli()