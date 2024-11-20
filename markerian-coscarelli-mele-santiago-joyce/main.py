
from app.gestionar_obra_imp import GestionarObraEspecifica
from app.mock_obra import runMock
from app.obra import Obra

import logging
#logger = logging.getLogger('peewee')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)

data_filepath = "markerian-coscarelli-mele-santiago-joyce/data/observatorio-de-obras-urbanas.csv"

#ETAPAS DEL SOFTWARE PRIMERO SE INICIA EL PROYECTO CON LA IMPLEMENTACION DE LA GESTION DE OBRA
# LOS PARAMETROS NONE Y NONE SON A FUTURO LA DB Y Y EL DATASET YA PROCESADO POR PANDAS
gestionObra = GestionarObraEspecifica(None, None)

#CONEXION A LA DB
conexion_db = gestionObra.conectar_db()

#CREACION DE TABLAS  Y ESTRUCTURA DE LA DB
gestionObra.mapear_orm()

# EXTRACCION DE DATOS DEL DATASET PUBLICO
gestionObra.extraer_datos(data_filepath)

# LIMPIEZA DE DATOS BASURA
gestionObra.limpiar_datos()

#POPULACION DE LA DB CON LOS DATOS DEL DATASET
gestionObra.cargar_datos()   

# INGRESO DE LOS DATOS DE LA NUEVA OBRA, ESTO YA PERSISTE EN DB
#nueva_obra_creada = gestionObra.nueva_obra()
nueva_obra_creada = gestionObra.nueva_obra_mock()
# LO QUE INGRESO EL USUARIO SE PASA A LA CLASE OBRA PARA PODER GESTIONAR LA MISMA
nuevo_proyecto_obra = Obra(nueva_obra_creada)
nuevo_proyecto_obra.nuevo_proyecto()
nuevo_proyecto_obra.iniciar_contratacion()
nuevo_proyecto_obra.adjudicar_obra()
nuevo_proyecto_obra.adjudicar_obra()
nuevo_proyecto_obra.actualizar_porcentaje_avance()
nuevo_proyecto_obra.incrementar_plazo()
nuevo_proyecto_obra.incrementar_mano_obra()
nuevo_proyecto_obra.finalizar_obra()
nuevo_proyecto_obra.rescindir_obra()


#runMock()



