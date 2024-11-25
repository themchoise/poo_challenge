import os
from peewee import SqliteDatabase
from sqlite3 import OperationalError
from app.helpers import check_etl
import json

db_path = './observatorio_de_obras_urbanas.db'
db = None
ETL_STATUS_FILE = "markerian-coscarelli-mele-vanotti-joyce/etl_status.json"
    

def crear_o_conectar_bd(db_path):
    status_etl = check_etl.check_etk_status()
    if os.path.exists(db_path) and not status_etl:
        try:
            print(f"El archivo de la base de datos '{db_path}' ya existe. Eliminándolo...")
            os.remove(db_path)
            print("Base de datos eliminada exitosamente.")
        except OSError as e:
            print(f"Error al intentar eliminar la base de datos: {e}")
            return None

    # Intentar conectar a la base de datos
    try:
        print('Intentando conectar a la base de datos ->')
        db = SqliteDatabase(db_path, pragmas={'journal_mode': 'wal'})
        db.connect()
        print('Base de datos conectada exitosamente.')
        return db
    except OperationalError as e:
        print("Error al conectar a la base de datos:", e)
        return None

def cerrar_conexion(db):
    """
    Función para cerrar la conexión a la base de datos.

    :param db: Instancia de la base de datos conectada.
    """
    if db and not db.is_closed():
        db.close()
        print("Conexión a la base de datos cerrada.")


db = crear_o_conectar_bd(db_path)