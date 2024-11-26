
import os
import sys
from app.gestionar_obra_imp import GestionarObraEspecifica
from app.obra import Obra
from app.db import crear_o_conectar_bd, cerrar_conexion
from app.helpers import check_etl
from app.mapa import mapa

import logging

#logger = logging.getLogger('peewee')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)

db_path = './observatorio_de_obras_urbanas.db'

data_filepath = "markerian-coscarelli-mele-vanotti-joyce/data/observatorio-de-obras-urbanas.csv"

status_etl = check_etl.check_etk_status()
# Verifica si el archivo existe antes de intentar abrirlo
status_p =   ' Ya ejecutado' if status_etl else ' No ejecutado'

gestionObra = GestionarObraEspecifica(None, None)

#CONEXION A LA DB
conexion_db = gestionObra.conectar_db()

if not status_etl:
    
    gestionObra.mapear_orm()
    # EXTRACCION DE DATOS DEL DATASET PUBLICO
    gestionObra.extraer_datos(data_filepath)

    # LIMPIEZA DE DATOS BASURA
    gestionObra.limpiar_datos()
    #POPULACION DE LA DB CON LOS DATOS DEL DATASET1
    gestionObra.cargar_datos() 
else:
    print("Proceso ETL Omitido")
  


obra_actual = None

obra_actual = None
proyecto_obra = None

def menu():
    global obra_actual, proyecto_obra
    while True:
        print("\nMenú de opciones:")
        print("1. Crear una nueva obra")
        print("2. Iniciar un nuevo proyecto para la obra")
        print("3. Iniciar contratación de la obra")
        print("4. Adjudicar obra")
        print("5. Actualizar porcentaje de avance")
        print("6. Incrementar plazo de obra")
        print("7. Incrementar mano de obra")
        print("8. Finalizar obra")
        print("9. Rescindir obra")
        print("10. Reiniciar Proceso ETL")
        print("11. Menu de Indicadores")
        print("12. Mapa de Obras")
        print("13. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            if obra_actual is None and proyecto_obra is None:
                obra_actual = crear_nueva_obra()
                proyecto_obra = Obra(obra_actual)  
            else:
                print("Ya existe una obra creada. No puede crear otra.")
        elif opcion == '2':
            if proyecto_obra:
                proyecto_obra.nuevo_proyecto()
                print("Proyecto iniciado con éxito.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '3':
            if proyecto_obra:
                proyecto_obra.iniciar_contratacion()
                print("Contratación iniciada con éxito.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '4':
            if proyecto_obra:
                proyecto_obra.adjudicar_obra()
                print("Obra adjudicada con éxito.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '5':
            if proyecto_obra:
                proyecto_obra.actualizar_porcentaje_avance()
                print("Porcentaje de avance actualizado.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '6':
            if proyecto_obra:
                proyecto_obra.incrementar_plazo()
                print("Plazo incrementado.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '7':
            if proyecto_obra:
                proyecto_obra.incrementar_mano_obra()
                print("Mano de obra incrementada.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '8':
            if proyecto_obra:
                proyecto_obra.finalizar_obra()
                print("Obra finalizada con éxito.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '9':
            if proyecto_obra:
                proyecto_obra.rescindir_obra()
                print("Obra rescindida con éxito.")
            else:
                print("No hay una obra creada. Cree una obra primero.")
        elif opcion == '10':
            print("Reiniciando ETL...")
            check_etl.reset_etl()
            python = sys.executable
            os.execl(python, python, *sys.argv)
            sys.re()
                  
        elif opcion == '11':
            
            gestionObra.obtener_indicadores()   
        elif opcion == '12':
            mapa(gestionObra.obtener_coordenadas() )    
        elif opcion == '13':
            print("Saliendo del programa...")
            cerrar_conexion(conexion_db)
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.")

def crear_nueva_obra():
    print("\nCreando una nueva obra...")
    nueva_obra_creada = gestionObra.nueva_obra()
    print(f"Nueva obra creada")
    return nueva_obra_creada

if __name__ == "__main__":
    menu()