from app import  importar_csv
from app import modelo_orm


data_filepath = "markerian-coscarelli-mele-santiago-joyce\data\observatorio-de-obras-urbanas.csv"

datos_importados = importar_csv.importar_datos(data_filepath)

modelo_orm.crear_db()

print(datos_importados)