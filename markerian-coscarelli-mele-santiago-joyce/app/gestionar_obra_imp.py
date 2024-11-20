
import datetime
import pandas as pd
from app.gestionar_obra import GestionarObra
from peewee import *
from peewee import fn
from app.modelo_obra import GestionObraModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable, Barrio,Licitacion_oferta_empresa, ContratacionTipo,Financiamiento
from app.db.database import db
from app.helpers import buscar_registro

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
   def extraer_datos(self, path) -> GestionObraModel:
     try:
        df = pd.read_csv(path, sep=";", index_col=None, encoding='latin-1')
        print('Datos Extraidos')
        self._df = df
     except FileNotFoundError as e:
        print("Error al conectar con el dataset.")
        return False
     
   def mapear_orm(self):
      print('Inicio de Mapeo al ORM')
      self._db.create_tables([ Entorno, Etapa, Tipo, AreaResponsable,Barrio, Licitacion_oferta_empresa, GestionObraModel, ContratacionTipo, Financiamiento], safe=True)
      print('Fin del Mapeo al  ORM')
   
   def limpiar_datos(self):
       print('Inicio Limpieza')
       self._df.dropna(how='all', inplace=True)
       self._df.fillna(value='', inplace=True)  
       print('Fin Limpeza')

   def cargar_datos(self):
      area_responsable_unicos = list(self._df['area_responsable'].dropna().unique())
      area_responsable_list = [AreaResponsable(area_responsable=area_responsable_unicos[i]) for i in range(len(area_responsable_unicos))]
      AreaResponsable.bulk_create(area_responsable_list)

      financiamiento_unicos = list(self._df['financiamiento'].dropna().unique())
      financiamiento_unicos.insert(0,'No Definido')
      financiamiento_list = [Financiamiento(financiamiento=financiamiento_unicos[i]) for i in range(len(financiamiento_unicos))]
      Financiamiento.bulk_create(financiamiento_list)

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
      licitacion_oferta_empresa.insert(0,'No Definido')
      licitacion_oferta_empresa_list = [Licitacion_oferta_empresa(licitacion_oferta_empresa=licitacion_oferta_empresa[i]) for i in range(len(licitacion_oferta_empresa))]
      Licitacion_oferta_empresa.bulk_create(licitacion_oferta_empresa_list)

      contratacion_tipo = list(self._df['contratacion_tipo'].dropna().unique())
      contratacion_tipo.insert(0,'No Definido')
      contratacion_tipo_list = [ContratacionTipo(contratacion_tipo=contratacion_tipo[i]) for i in range(len(contratacion_tipo))]
      ContratacionTipo.bulk_create(contratacion_tipo_list)

   def nueva_obra(self):
     
      print("Ingreso de nueva obra")
      print("Por favor, ingresa los siguientes datos:")
     
      entorno_nombre = input("Entorno, ejemplo(Acumar, Paseo Del Bajo): ")
      entorno = buscar_registro.buscar_registro(entorno_nombre, Entorno, 'entorno')


      tipo_nombre = input("Tipo, ejemplo(Vivienda, Escuelas): ")
      tipo = buscar_registro.buscar_registro(tipo_nombre, Tipo, 'tipo')

      area_nombre = input("Área Responsable, ejemplo(Instituto de la Vivienda): ")
      area = buscar_registro.buscar_registro(area_nombre, AreaResponsable, 'area_responsable')

      barrio_nombre = input("Barrio, ejemplo(Montserrat): ")
      barrio = buscar_registro.buscar_registro(barrio_nombre, Barrio, 'barrio')

      # Los valores 0 hacen referencia al Dato no definido
      # Etapa 5 significa "En Obra"
     
      datos = {
        "entorno": entorno,
        "nombre": input("Nombre de la obra: "),
        "etapa": 5,
        "tipo": tipo,
        "area_responsable": area,
        "barrio": barrio,
        "direccion": input("Dirección: "),
        "licitacion_oferta_empresa": 0,
        "contratacion_tipo": 0,
        "financiamiento": 0
      }
      nueva_obra = GestionObraModel(**datos)
      return nueva_obra.save()
   
   # Este metodo se usa para generar una obra ficticia
   def nueva_obra_mock(self):
      # Los valores 0 hacen referencia al Dato no definido
      # Etapa 5 significa "En Obra"
     
      datos = {
        "entorno": 1,
        "nombre": "Obra Mock",
        "etapa": 5,
        "tipo": 1,
        "area_responsable": 1,
        "barrio": 1,
        "direccion": "Fake Street 321",
        "licitacion_oferta_empresa": 0,
        "contratacion_tipo": 0,
        "financiamiento": 0
      }
      nueva_obra_mock = GestionObraModel(**datos)
      nueva_obra_mock.save()
      return nueva_obra_mock


   

   def obtener_indicadores(self):
      print("""a. Listado de todas las áreas responsables. 
               b. Listado de todos los tipos de obra. 
               c. Cantidad de obras que se encuentran en cada etapa. 
               d. Cantidad de obras y monto total de inversión por tipo de obra. 
               e. Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3. 
               f. Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1. 
               g. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
               h. Porcentaje total de obras finalizadas. 
               i. Cantidad total de mano de obra empleada. 
               j. Monto total de inversión. """)
      print("Listado de todas las áreas responsables")
      areas_responsables =  AreaResponsable.select()
      areas_responsables_data = [{  **area_responsable.__data__} for area_responsable in areas_responsables ]
      print(areas_responsables_data)
      print("")

      print("Listado de todos los tipos de obra. ")
      tipo_obras =  Tipo.select()
      tipo_obras_data = [{  **tipo_obra.__data__} for tipo_obra in tipo_obras ]
      print(tipo_obras_data)
      print("")

      #Cantidad de obras que se encuentran en cada etapa.
      print("Cantidad de obras que se encuentran en cada etapa.")
      query = (GestionObraModel
         .select(GestionObraModel.nombre, fn.COUNT(GestionObraModel.etapa).alias('total'))
         .group_by(GestionObraModel.nombre)
         .order_by(GestionObraModel.nombre))

      for nombre, total in query.tuples():
         print(nombre, total)

      print("")
      #Cantidad de obras y monto total de inversión por tipo de obra. 
      query_cantidad_obras = (GestionObraModel
         .select(fn.COUNT('*')))
      cantidad_obras = query_cantidad_obras.scalar()
      print(f'Total de obras -> {cantidad_obras}')

      print("")

      query_inversion = (GestionObraModel
         .select(Tipo.tipo, fn.SUM(GestionObraModel.monto_contrato).alias('total_monto_contrato'))
         .join(Tipo, on=(GestionObraModel.tipo == Tipo.id))
         .group_by(GestionObraModel.tipo)
         .order_by(GestionObraModel.tipo))
      
      print(" monto total de inversión por tipo de obra")
      for tipo, total_monto_contrato in query_inversion.tuples():
         print(tipo, total_monto_contrato)
      #obras =  GestionObraModel.select()
      #obras_data= [ { **obra.__data__}for obra in obras ]

      print("")
      #Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3. 
      comunas_ids = [1, 2, 3]
      query_barrios = (GestionObraModel
         .select(Barrio.barrio)
         .join(Barrio, on=(GestionObraModel.barrio == Barrio.id))
         .where(GestionObraModel.comuna << comunas_ids)
         .order_by(GestionObraModel.barrio))   
      print("Barrios de comunas 1 2 y 3")
      for barrio in query_barrios.tuples():
         print(barrio)      
      
      #Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1. 
      print("")
      print("Cantidad de obras finalizadas y su y monto total de inversión en la comuna 1.") 
      comuna_busqueda = 1
      comuna_busqueda = 1
      query_inversion_comuna_uno = (
         GestionObraModel
         .select(
            fn.COUNT(GestionObraModel.id).alias('cantidad_finalizad'), 
            fn.SUM(GestionObraModel.monto_contrato).alias('monto_total')   )
         .where(  (GestionObraModel.comuna == comuna_busqueda) &  (GestionObraModel.etapa == 1) )   )

      for cantidad_finalizad, monto_total in query_inversion_comuna_uno.tuples():
         print(f'Cantidad finalizad -> {cantidad_finalizad}, monto total -> {monto_total}')         


      print("") 
       # Cantidad de obras finalizadas en un plazo menor o igual a 24 meses.
      querty_obras_finalizadas_plazo = (
         GestionObraModel
         .select( fn.COUNT(GestionObraModel.id).alias('cantidad_finalizad'))
         .where(  GestionObraModel.plazo_meses <= '24'     ) )
      
      print("Cantidad de obras finalizadas en un plazo menor o igual a 24 meses. -> " + str(querty_obras_finalizadas_plazo.scalar()))


      #Total Obras
      #h. Porcentaje total de obras finalizadas. 
      query_total_obras = (
         GestionObraModel
         .select(fn.COUNT(GestionObraModel.id).alias('total_obras'))
      )
      total_obras = query_total_obras.scalar()


      querty_porcentaje_finalizadas = (
         GestionObraModel
         .select( fn.COUNT(GestionObraModel.id).alias('porcentaje_finalizad'))
         .where(  GestionObraModel.etapa == 1   ) )
      total_obras_finalizadas = querty_porcentaje_finalizadas.scalar()
      porcentaje_finalizadas =  round(( total_obras_finalizadas / total_obras  )*100,2)
      
      print(f'Porcentaje total de obras finalizadas. -> {porcentaje_finalizadas}% ')
      print("")

      #Cantidad total de mano de obra empleada. 
      query_total_mano_de_obra = (
         GestionObraModel
         .select(fn.SUM(GestionObraModel.mano_obra).alias('total_mano_obra'))
      )
      total_mano_de_obra = query_total_mano_de_obra.scalar()
      print(f'total_mano_de_obra -> {total_mano_de_obra}')


      #Monto total de inversion 
      query_total_inversion = (
         GestionObraModel
         .select(fn.SUM(GestionObraModel.monto_contrato).alias('total_inversion'))
      )
      total_inversion = query_total_inversion.scalar()
      print(f'total_inversion -> {total_inversion}')
      
         
     

     
     
     