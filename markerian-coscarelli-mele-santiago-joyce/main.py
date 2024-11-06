from app import  importar_csv

data_filepath = "./data/observatorio-de-obras-urbanas.csv"

datos_importados = importar_csv.importar_datos(data_filepath)

print(datos_importados)