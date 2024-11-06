import pandas as pd

def importar_datos_csv():
    """ Cantidad de viajes diarios realizados en transporte público de la Ciudad Autónoma de Buenos Aires según modo de transporte. Incluye tipo de transporte, día, si la información es parcial o completa y cantidad de viajes. """
    
    archivo_csv = "./importar_csv_a_base_datos/dataset_viajes_sube.csv"
    #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/sube/dataset_viajes_sube.csv"

    try:
        df = pd.read_csv(archivo_csv, sep=",")
        return df
    except FileNotFoundError as e:
        print("Error al conectar con el dataset.", e)
        return False