
from app import modelo_orm
from app.gestionar_obra_imp import GestionarObraEspecifica
import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

data_filepath = "markerian-coscarelli-mele-santiago-joyce/data/observatorio-de-obras-urbanas.csv"


nueva_obra = GestionarObraEspecifica(None, None)
conexion_db = nueva_obra.conectar_db()
nueva_obra.mapear_orm()
nueva_obra.extraer_datos(data_filepath)
nueva_obra.limpiar_datos()
nueva_obra.cargar_datos()   

