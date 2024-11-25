
import pandas as pd
from app.gestionar_obra import GestionarObra
from peewee import *
from peewee import fn
from app.modelo_obra import GestionObraModel
from app.models import Entorno, Etapa, Tipo, AreaResponsable, Barrio,Licitacion_oferta_empresa, ContratacionTipo,Financiamiento
from app.db.database import db
from app.helpers import buscar_registro
from app.helpers import check_etl


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
               db.connect() 

      
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
      print("Inicio de la carga de datos")
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

      tamanio_dataset = self._df.shape[0]

      print(f'Rows a Insertar segun dataset -> {tamanio_dataset} \n')
      for index, row in self._df.iterrows():
         porcentaje = (index + 1) / tamanio_dataset * 100
         print(f"\033[FProgreso: {porcentaje:.2f}%")
         datos_popular = {
         "entorno": Entorno.select().where(Entorno.entorno == row['entorno']).limit(1).first(),
         "nombre": row['nombre'],
         "etapa": Etapa.select().where(Etapa.etapa == row['etapa']).limit(1).first(),
         "tipo": Tipo.select().where(Tipo.tipo == row['tipo']).limit(1).first(),
         "area_responsable": AreaResponsable.select().where(AreaResponsable.area_responsable == row['area_responsable']).limit(1).first(),
         "descripcion": row['descripcion'],
         "monto_contrato": row['monto_contrato'],
         "comuna": row['comuna'],
         "barrio": Barrio.select().where(Barrio.barrio == row['barrio']).limit(1).first(),
         "direccion": row['direccion'],
         "lat": row['lat'],
         "lng": row['lng'],
         "fecha_inicio": row['fecha_inicio'],
         "fecha_fin_inicial": row['fecha_fin_inicial'],
         "plazo_meses": row['plazo_meses'],
         "porcentaje_avance": row['porcentaje_avance'],
         "imagen_1": row['imagen_1'],
         "imagen_2": row['imagen_2'],
         "imagen_3": row['imagen_3'],
         "imagen_4": row['imagen_4'],
         "licitacion_oferta_empresa": row['licitacion_oferta_empresa'],
         "licitacion_anio": row['licitacion_anio'],
         "contratacion_tipo": row['contratacion_tipo'],
         "nro_contratacion": row['nro_contratacion'],
         "cuit_contratista": row['cuit_contratista'],
         "beneficiarios": row['beneficiarios'],
         "mano_obra": row['mano_obra'],
         "compromiso": row['compromiso'],
         "destacada": row['destacada'],
         "ba_elige": row['ba_elige'],
         "link_interno": row['link_interno'],
         "pliego_descarga": row['pliego_descarga'],
         "expediente_numero": row['expediente-numero'],
         "estudio_ambiental_descarga": row['estudio_ambiental_descarga'],
         "financiamiento": row['financiamiento'],
         }

         try:
            obra_pulada = GestionObraModel(**datos_popular) 
            obra_pulada.save()  
         except IntegrityError as e:
            print(f"Error de integridad al guardar la obra '{datos_popular.get('nombre', 'Desconocido')}': {e}")
         except DatabaseError as e:
            print(f"Error de base de datos al guardar la obra '{datos_popular.get('nombre', 'Desconocido')}': {e}")
         except Exception as e:
            print(f"Error desconocido al guardar la obra '{datos_popular.get('nombre', 'Desconocido')}': {e}")

      check_etl.set_etl()    
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
      nueva_obra.save()
      return nueva_obra
   
   def obtener_indicadores(self):
      def mostrar_menu():
         print("\n" + "=" * 50)
         print("               GESTIÓN DE OBRAS")
         print("=" * 50)
         print("1. Listado de todas las áreas responsables")
         print("2. Listado de todos los tipos de obra")
         print("3. Cantidad de obras que se encuentran en cada etapa")
         print("4. Cantidad de obras y monto total de inversión por tipo de obra")
         print("5. Listado de todos los barrios en las comunas 1, 2 y 3")
         print("6. Obras finalizadas y monto total de inversión en la comuna 1")
         print("7. Cantidad de obras finalizadas en un plazo menor o igual a 24 meses")
         print("8. Porcentaje total de obras finalizadas")
         print("9. Cantidad total de mano de obra empleada")
         print("10. Monto total de inversión")
         print("0. Salir")
         print("=" * 50)

      def ejecutar_opcion(opcion):
         if opcion == 1:
            print("\n--- Listado de todas las áreas responsables ---")
            areas_responsables = AreaResponsable.select()
            for area in areas_responsables:
                  print(area.__data__)
         
         elif opcion == 2:
            print("\n--- Listado de todos los tipos de obra ---")
            tipos_obra = Tipo.select()
            for tipo in tipos_obra:
                  print(tipo.__data__)
         
         elif opcion == 3:
            print("\n--- Cantidad de obras por etapa ---")
            query = (GestionObraModel
                     .select(GestionObraModel.nombre, fn.COUNT(GestionObraModel.etapa).alias('total'))
                     .group_by(GestionObraModel.nombre)
                     .order_by(GestionObraModel.nombre))
            for nombre, total in query.tuples():
                  print(f"{nombre}: {total}")
         
         elif opcion == 4:
            print("\n--- Obras y monto total por tipo de obra ---")
            query = (GestionObraModel
                     .select(Tipo.tipo, fn.SUM(GestionObraModel.monto_contrato).alias('total'))
                     .join(Tipo, on=(GestionObraModel.tipo == Tipo.id))
                     .group_by(GestionObraModel.tipo))
            for tipo, total in query.tuples():
                  print(f"{tipo}: {total}")
         
         elif opcion == 5:
            print("\n--- Barrios en las comunas 1, 2 y 3 ---")
            comunas_ids = [1, 2, 3]
            query = (GestionObraModel
                     .select(Barrio.barrio)
                     .join(Barrio, on=(GestionObraModel.barrio == Barrio.id))
                     .where(GestionObraModel.comuna << comunas_ids))
            for barrio in query.tuples():
                  print(barrio)
         
         elif opcion == 6:
            print("\n--- Obras finalizadas y monto en la comuna 1 ---")
            query = (GestionObraModel
                     .select(fn.COUNT(GestionObraModel.id).alias('cantidad'),
                              fn.SUM(GestionObraModel.monto_contrato).alias('monto'))
                     .where((GestionObraModel.comuna == 1) & (GestionObraModel.etapa == 1)))
            for cantidad, monto in query.tuples():
                  print(f"Obras: {cantidad}, Monto: {monto}")
         
         elif opcion == 7:
            print("\n--- Obras finalizadas en ≤ 24 meses ---")
            query = (GestionObraModel
                     .select(fn.COUNT(GestionObraModel.id).alias('cantidad'))
                     .where(GestionObraModel.plazo_meses <= 24))
            print(f"Cantidad: {query.scalar()}")
         
         elif opcion == 8:
            print("\n--- Porcentaje de obras finalizadas ---")
            total = GestionObraModel.select(fn.COUNT(GestionObraModel.id)).scalar()
            finalizadas = GestionObraModel.select(fn.COUNT(GestionObraModel.id)).where(GestionObraModel.etapa == 1).scalar()
            porcentaje = round((finalizadas / total) * 100, 2) if total > 0 else 0
            print(f"Porcentaje: {porcentaje}%")
         
         elif opcion == 9:
            print("\n--- Total de mano de obra empleada ---")
            total_mano_obra = (GestionObraModel
                                 .select(fn.SUM(GestionObraModel.mano_obra))
                                 .scalar())
            print(f"Mano de obra total: {total_mano_obra}")
         
         elif opcion == 10:
            print("\n--- Monto total de inversión ---")
            total_inversion = (GestionObraModel
                                 .select(fn.SUM(GestionObraModel.monto_contrato))
                                 .scalar())
            print(f"Monto total: {total_inversion}")
         
         elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
         
         else:
            print("Opción inválida. Intente nuevamente.")

      while True:
         mostrar_menu()
         try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 0:
                  ejecutar_opcion(opcion)
                  break
            ejecutar_opcion(opcion)
         except ValueError:
            print("Por favor, ingrese un número válido.")
