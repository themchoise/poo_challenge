
import pandas as pd
from gestionar_obra import GestionarObra
from peewee import *


class GestionarObraEspecifica(GestionarObra):
    def conectar_db(self):
     try:
        sqlite_db = SqliteDatabase('./observatorio_de_obras_urbanas.db', pragmas={'journal_mode': 'wal'})
        sqlite_db.connect()
     except OperationalError as e:
        print("Error al conectar con la BD.", e)
        exit()


# A ESTE METODO SE LE PASA EL PATH DEL CSV Y DEVUELVE LOS DATOS EN FORMATO DATAFRAME
    def extraer_datos(self, path):
     try:
        return pd.read_csv(path, sep=";", index_col=0, encoding='latin-1')
     except FileNotFoundError as e:
        print("Error al conectar con el dataset.")
        return False
     
     
     