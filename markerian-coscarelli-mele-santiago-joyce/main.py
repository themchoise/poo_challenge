
from app.gestionar_obra_imp import GestionarObraEspecifica
from app.mock_obra import runMock
import logging
#logger = logging.getLogger('peewee')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)

data_filepath = "markerian-coscarelli-mele-santiago-joyce/data/observatorio-de-obras-urbanas.csv"


gestionObra = GestionarObraEspecifica(None, None)
conexion_db = gestionObra.conectar_db()
gestionObra.mapear_orm()
gestionObra.extraer_datos(data_filepath)
gestionObra.limpiar_datos()
gestionObra.cargar_datos()   
#gestionObra.nueva_obra()
runMock()
obras = gestionObra.obtener_indicadores()   
print(obras)


