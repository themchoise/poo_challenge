from peewee import fn

def buscar_registro(valor, modelo, atributo):
    registro = None
    while registro is None:
        try:
            print(f'Buscando {atributo} -> {valor}')
            registro = modelo.select().where(
                fn.Lower(fn.Trim(getattr(modelo, atributo))) == valor.strip().lower()
            ).limit(1).offset(0)
            if registro.exists():
                print(f'{atributo.capitalize()} encontrado: {registro[0]}')
            else:
                raise modelo.DoesNotExist

        except modelo.DoesNotExist:
            print(f'El {atributo} "{valor}" no encontrado, por favor ingrese un nuevo valor.')
            valor = input(f"{atributo.capitalize()} Nueva Búsqueda: ")
            registro = None
    return registro[0]  # Regresa el primer (y único) resultado encontrado
