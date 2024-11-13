from app import  importar_csv
from app import modelo_orm
from app.gestionar_obra_imp import GestionarObraEspecifica



data_filepath = "markerian-coscarelli-mele-santiago-joyce\data\observatorio-de-obras-urbanas.csv"

datos_importados = importar_csv.importar_datos(data_filepath)

nueva_obra = GestionarObraEspecifica()
conexion_db = nueva_obra.conectar_db()

# print(conexion_db)
#print(datos_importados)


