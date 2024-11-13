
from sqlite3 import OperationalError
from peewee import SqliteDatabase

db = None
try:
    print('Intentando conectar a la db ->')
    db = SqliteDatabase('./observatorio_de_obras_urbanas.db', pragmas={'journal_mode': 'wal'})    
    print('Base de datos creada exitosamente')
except OperationalError as e:
    print("Error al crear  la BD.", e)
    exit()