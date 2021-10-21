import os

from peewee import SqliteDatabase

class dev():
  DEBUG = True
  SECRET_KEY = os.urandom(24)
  DATABASE = {
    'name' : 'dbTest.sqlite3',
    'engine' : 'peewee.SqliteDatabase' 
  }

class prod():
  DEBUG = False
  SECRET_KEY = os.urandom(24)
  DATABASE = {
    'name' : 'hotel.sqlite3',
    'engine' : 'peewee.SqliteDatabase',
    'host' : 'url',
    'user' : 'user1',
    'password' : '123456'
  }
