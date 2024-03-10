import os
import sqlite3


def init_db():
    ruta_relativa='modulo4/ejercicios/archivos_relativos/base_datos.db'
    directorio=os.getcwd()
    rabsoluta=os.path.join(directorio,ruta_relativa)
    conexion=sqlite3.connect(rabsoluta)
    return conexion