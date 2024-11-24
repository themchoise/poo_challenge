from peewee import fn

def buscar_registro(valor, modelo, atributo):
    """
    Busca un registro en un modelo especificado, bloqueando la ejecución hasta encontrarlo.
    """
    registro = None
    while registro is None:
        try:
            print(f'Buscando {atributo} -> {valor}')
            registro = modelo.select().where(
                fn.Lower(fn.Trim(getattr(modelo, atributo))) == valor.strip().lower()
            ).limit(1).first() 
            if registro:  
                print(f'{atributo.capitalize()} encontrado: {getattr(registro, atributo)}')
                return registro
            else:
                raise modelo.DoesNotExist
        except modelo.DoesNotExist:
            print(f'El {atributo} "{valor}" no encontrado, por favor ingrese un nuevo valor.')
            valor = input(f"{atributo.capitalize()} Nueva Búsqueda: ")
