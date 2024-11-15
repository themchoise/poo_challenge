
import pandas as pd
from app.gestionar_obra import GestionarObra
from peewee import *
from app.modelo_obra import GestionObraModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable, Barrio,Licitacion_oferta_empresa, ContratacionTipo
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
         # Verificar si la base de datos está cerrada y conectarla si es necesario
         if db.is_closed():
               db.connect()  # Conectar la base de datos si está cerrada

         # Asignar la conexión de base de datos al atributo `self._db`
         self._db = db
         return db

      except OperationalError as e:
         print("Error al conectar con la base de datos:", e)
         return None


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
      self._db.create_tables([ Entorno, Etapa, Tipo, AreaResponsable,Barrio, Licitacion_oferta_empresa, GestionObraModel, ContratacionTipo], safe=True)
      print('Fin del Mapeo al  ORM')
   
   def limpiar_datos(self):
       print('Inicio Limpieza')
       self._df.dropna(how='all', inplace=True)
       self._df.fillna(value='', inplace=True)  
       print('Fin Limpeza')

   def cargar_datos(self):
      print(self._db)
      area_responsable_unicos = list(self._df['area_responsable'].dropna().unique())
      area_responsable_list = [AreaResponsable(area_responsable=area_responsable_unicos[i]) for i in range(len(area_responsable_unicos))]
      AreaResponsable.bulk_create(area_responsable_list)

      entorno_unicos = list(self._df['entorno'].dropna().unique())
      entorno_unicos_list = [Entorno(entorno=entorno_unicos[i]) for i in range(len(entorno_unicos))]
      Entorno.bulk_create(entorno_unicos_list)

      etapa_unicos = list(self._df['etapa'].dropna().unique())
      etapa_unicos_list = [Etapa(etapa=etapa_unicos[i]) for i in range(len(etapa_unicos))]
      Etapa.bulk_create(etapa_unicos_list)
   
      tipo_unicos = list(self._df['tipo'].dropna().unique())
      tipo_unicos_list = [Tipo(tipo=tipo_unicos[i]) for i in range(len(tipo_unicos))]
      Tipo.bulk_create(tipo_unicos_list)

      barrio = list(self._df['barrio'].dropna().unique())
      barrio_list = [Barrio(barrio=barrio[i]) for i in range(len(barrio))]
      Barrio.bulk_create(barrio_list)

      licitacion_oferta_empresa = list(self._df['licitacion_oferta_empresa'].dropna().unique())
      licitacion_oferta_empresa_list = [Licitacion_oferta_empresa(licitacion_oferta_empresa=licitacion_oferta_empresa[i]) for i in range(len(licitacion_oferta_empresa))]
      Licitacion_oferta_empresa.bulk_create(licitacion_oferta_empresa_list)

      contratacion_tipo = list(self._df['contratacion_tipo'].dropna().unique())
      contratacion_tipo_list = [ContratacionTipo(contratacion_tipo=contratacion_tipo[i]) for i in range(len(contratacion_tipo))]
      ContratacionTipo.bulk_create(contratacion_tipo_list)

      

      
       

     

     
     
     