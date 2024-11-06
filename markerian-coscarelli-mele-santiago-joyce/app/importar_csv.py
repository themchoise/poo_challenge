import pandas as pd
from pandas import DataFrame
def importar_datos(path:str) -> DataFrame | bool:

    try:
          return pd.read_csv(path, sep=";",  index_col=0, encoding='latin-1')
    except FileNotFoundError as e:
        print("Error al conectar con el dataset.")
        return False