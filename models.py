from peewee import *
from playhouse.flask_utils import FlaskDB

from app import habitacion

db = FlaskDB()

class Usuario(db.Model):
  username = TextField(primary_key=True)
  password = TextField()
  nombre = TextField()
  apellido = TextField()
  rol = IntegerField() # 0=superadmin, 1=admin, 2=cliente

class Cliente(db.Model):
  usuario = ForeignKeyField(Usuario, primary_key=True)
  telefono = TextField()
  email = TextField() # Debe ser unico
  direccion = TextField()
  genero = IntegerField() # 0=M, 1=F, 2=Otro
  # fecha_nacimiento = DateField()

class Habitacion(db.Model):
  id = AutoField(primary_key=True)
  precio = FloatField()
  cant_personas = IntegerField()
  disponible = BooleanField()

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


