import os
from peewee import SqliteDatabase
from sqlite3 import OperationalError


db_path = './observatorio_de_obras_urbanas.db'


if os.path.exists(db_path):
    try:
        print(f"El archivo de la base de datos '{db_path}' ya existe. Eliminándolo...")
        os.remove(db_path)
        print("Base de datos eliminada exitosamente.")
    except OSError as e:
        print(f"Error al intentar eliminar la base de datos: {e}")
        exit()


try:
    print('Intentando conectar a la base de datos ->')
    db = SqliteDatabase(db_path, pragmas={'journal_mode': 'wal'})
    db.connect()  
    print('Base de datos conectada exitosamente')
except OperationalError as e:
    print("Error al conectar a la base de datos:", e)
    exit()


def cerrar_conexion():
    if not db.is_closed():
        db.close()
        print("Conexión a la base de datos cerrada.")
