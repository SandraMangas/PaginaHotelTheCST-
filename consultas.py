from app import *

@app.cli.command("crear_datos_iniciales")
def consultar_datos():
  db.init_app(app)

  