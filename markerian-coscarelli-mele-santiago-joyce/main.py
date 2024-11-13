
from app import modelo_orm
from app.gestionar_obra_imp import GestionarObraEspecifica



data_filepath = "markerian-coscarelli-mele-santiago-joyce/data/observatorio-de-obras-urbanas.csv"


nueva_obra = GestionarObraEspecifica(None, None)
conexion_db = nueva_obra.conectar_db()
nueva_obra._db=conexion_db
nueva_obra.mapear_orm()
nueva_obra.extraer_datos(data_filepath)
nueva_obra.limpiar_datos()
nueva_obra.cargar_datos()

