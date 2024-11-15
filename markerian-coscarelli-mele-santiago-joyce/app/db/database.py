from peewee import SqliteDatabase
from sqlite3 import OperationalError

# Inicializa y configura la base de datos con modo WAL
try:
    print('Intentando conectar a la base de datos ->')
    db = SqliteDatabase('./observatorio_de_obras_urbanas.db', pragmas={'journal_mode': 'wal'})
    db.connect()  # Asegurarse de que esté conectada inmediatamente
    print('Base de datos conectada exitosamente')
except OperationalError as e:
    print("Error al conectar a la base de datos:", e)
    exit()

# Definir un método de cierre seguro
def cerrar_conexion():
    if not db.is_closed():
        db.close()
