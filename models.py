from peewee import *
from playhouse.flask_utils import FlaskDB

db = FlaskDB()

class Usuario(db.Model):
  username = TextField(primary_key=True)
  password = TextField()
  nombre = TextField()
  apellido = TextField()
  tipo_usuario = IntegerField() # 0=superadmin, 1=admin, 2=cliente
  deleted = IntegerField() # 0=deleted(hide), 1=active


class Cliente(db.Model):
  usuario = ForeignKeyField(Usuario, primary_key=True)
  telefono = TextField()
  email = TextField() # Debe ser unico
  direccion = TextField()
  # fecha_nacimiento = DateField()

class Habitacion(db.Model):
  id = TextField(primary_key=True)
  precio = FloatField()
  tipo_habitacion = IntegerField() # 0=economica, 1=sencilla, 2=doble, 3=romantica
  cant_personas = IntegerField()
  estado = IntegerField() # 0=inactiva, 1=disponible, 2=disponible
  deleted = IntegerField() # 0=deleted(hide), 1=active

class Calificacion(db.Model):
  id = AutoField()
  habitacion = ForeignKeyField(Habitacion, backref="calificaciones")
  cliente = ForeignKeyField(Cliente, backref="calificaciones")
  comentario = TextField()
  calificacion = IntegerField() # 0 min - 5 max

class Reserva(db.Model):
  id = AutoField()
  habitacion = ForeignKeyField(Habitacion, backref="reservas")
  usuario = ForeignKeyField(Usuario, backref="reservas")
  fecha_ingreso = DateField() #Format??
  fecha_salida = DateField() #Format??
  cant_personas = IntegerField()
  # estado = IntegerField() # 0=cancelada, 1=reservada, 2=disponible
  deleted = IntegerField() # 0=deleted(hide), 1=active


