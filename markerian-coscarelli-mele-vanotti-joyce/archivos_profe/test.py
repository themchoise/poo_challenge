from model_viajes_sube import *
from importar_viajes_sube import *

if __name__== "__main__" :
    df = importar_datos_csv()
    if df is False:
        exit()
    
    #Obtenemos información sobre la estructura del archivo csv
    print(df.head())
    print(df.count())
    print(df.columns)

    #Obtenemos desde el archivo csv el listado de los valores de tipo de transporte
    """ tipo_transporte = df['TIPO_TRANSPORTE']
    for x in tipo_transporte:
        print(f"{x}") """

    #Eliminar valores NA o NaN (nulos o no disponibles)
    df.dropna(subset = ["TIPO_TRANSPORTE"], axis = 0, inplace = True)

    #Obtener los valores únicos (no repetidos) de una columna
    data_unique = list(df['TIPO_TRANSPORTE'].unique())
    print(data_unique)

    #Eliminar valores NA o NaN (nulos o no disponibles)
    df.dropna(subset = ["CANTIDAD"], axis = 0, inplace = True)
    #print(df['CANTIDAD'])

    #Recorremos las filas del archivo csv e insertamos los valores de TipoTransporte en la tabla 'tipos_transporte' de la BD
    print("Recorremos las filas del archivo csv e insertamos los valores de TipoTransporte en la tabla 'tipos_transporte' de la BD")
    for elem in data_unique:
        print("Elemento:", elem)
        try:
            TipoTransporte.create(nombre=elem)
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla tipos_transporte.", e)
    print("Se han persistido los tipos de transporte en la BD.")
    
    #Recorremos las filas del archivo csv e insertamos los valores en la tabla 'viajes' de la BD
    print("Recorremos las filas del archivo csv e insertamos los valores en la tabla 'viajes' de la BD")
    for elem in df.values:
        tipo_transp = TipoTransporte.get(TipoTransporte.nombre == elem[0])
        try:
            ViajeSube.create(tipo_transporte=tipo_transp,date=elem[1], parcial=elem[2], quantity=elem[3])
        except IntegrityError as e:
            print("Error al insertar un nuevo registro en la tabla viajes.", e)
    print("Se han persistido los viajes en sube en la BD.")