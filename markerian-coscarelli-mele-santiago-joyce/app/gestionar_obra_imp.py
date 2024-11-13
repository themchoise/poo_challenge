
import pandas as pd
from app.gestionar_obra import GestionarObra
from peewee import *
from app.models.modelo_obra import GestionObraModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable
from app.db.database import db

class GestionarObraEspecifica(GestionarObra):

   def conectar_db(self):
     try:
        return db.connect()
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
     
   def mapear_orm(self):
      cnn = self.conectar_db()
      cnn.create_tables([ Entorno, Etapa, Tipo, AreaResponsable, GestionObraModel])

   def cargar_datos(self):
      return super().cargar_datos()
   
   def limpiar_datos(self):
      return super().limpiar_datos()
     

     
     
     