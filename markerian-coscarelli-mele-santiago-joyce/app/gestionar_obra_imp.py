
import pandas as pd
from app.gestionar_obra import GestionarObra
from peewee import *
from app.models.modelo_obra import GestionObraModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable
from app.db.database import db

class GestionarObraEspecifica(GestionarObra):

   def __init__(self, df, db):
      self._df = df  
      self._db = db  

   @property
   def df(self):
      return self._df 

   @df.setter
   def df(self, value):
      self._df = value 

   @property
   def db(self):
      return self._db 

   @db.setter
   def db(self, value):
      self._db = value 


   def conectar_db(self):
     try:
       if db.is_closed():
           self._df=db
           return db
       
       else:
           self._df=db
           return db.connect()
       
        
     except OperationalError as e:
        print("Error al conectar con la BD.", e)
        exit()


# A ESTE METODO SE LE PASA EL PATH DEL CSV Y DEVUELVE LOS DATOS EN FORMATO DATAFRAME
   def extraer_datos(self, path):
     try:
        df = pd.read_csv(path, sep=";", index_col=None, encoding='latin-1')
        print('Datos Extraidos')
        self._df = df
     except FileNotFoundError as e:
        print("Error al conectar con el dataset.")
        return False
     
   def mapear_orm(self):
      print('Inicio de Mapeo al ORM')
      self._db.create_tables([ Entorno, Etapa, Tipo, AreaResponsable, GestionObraModel])
      print('Fin del Mapeo al  ORM')
   
   def limpiar_datos(self):
       print('Inicio Limpieza')
       self._df.dropna(how='all', inplace=True)
       self._df.fillna(value='', inplace=True)  
       print('Fin Limpeza')

   def cargar_datos(self):
      print(self._db)
      datos_unicos = list(self._df['area_responsable'].dropna().unique())
      AreaResponsable.create(area_responsable="Hola")
      """
      for x in datos_unicos:
        if isinstance(x, str) and x.strip(): 
         try:
         
               AreaResponsable.create(area_responsable="Hola")
         except IntegrityError as e:
               print("Error al insertar un nuevo registro en la tabla area_responsable.", e)
      print("Se han persistido los tipos de transporte en la BD.")
      """
      
       

     

     
     
     