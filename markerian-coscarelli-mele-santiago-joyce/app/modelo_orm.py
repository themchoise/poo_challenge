from peewee import *

def crear_db():

    sqlite_db = SqliteDatabase('./observatorio_de_obras_urbanas.db', pragmas={'journal_mode': 'wal'})

    try:
        sqlite_db.connect()
    except OperationalError as e:
        print("Error al conectar con la BD.", e)
        exit()

class BaseModel(Model):
        class Meta:
            database = sqlite_db
