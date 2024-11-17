from datetime import datetime
import peewee
from peewee import *

# Clase ORM para representar una obra
class Obra:
    
    def __init__(self, obra_instance):
        self.obra = obra_instance  # La instancia de la obra de la base de datos

    def nuevo_proyecto(self):
        """Inicia un nuevo proyecto de obra"""
        try:
            # etapa_proyecto instancia del objeto de la db que se obtuvo si existia, o que se creo si no.
            # created = boolean true si fue creado en la db o false si el objeto ya existia en la db
            # Etapa clase de Peewee que representa la tabla etapa en la db
            # Obtener la etapa "Proyecto", si no existe, crearla en la tabla Etapa
            # nombre="Proyecto" filtro de campo
            etapa_proyecto, created = Etapa.get_or_create(nombre="Proyecto")
            
            # Asignar la etapa a la obra
            self.obra.etapa = etapa_proyecto
            self.obra.save()
            # Actualiza el campo etapa en la db para reflejar que la obra está en la fase de proyecto.
            print(f"Obra '{self.obra.nombre}' iniciada como Proyecto.")
        except Exception as e:
            print(f"Error al iniciar el proyecto: {e}")

    def iniciar_contratacion(self):
        """Inicia la contratación de la obra"""
        try:
            tipo_contratacion = input("Ingrese el tipo de contratación: ")
            tipo_contratacion_instance = TipoContratacion.get(TipoContratacion.nombre == tipo_contratacion)
            
            nro_contratacion = input("Ingrese el número de contratación: ")
            self.obra.tipo_contratacion = tipo_contratacion_instance
            self.obra.nro_contratacion = nro_contratacion
            self.obra.save()
            print(f"Contratación de la obra '{self.obra.nombre}' iniciada.")
        except peewee.DoesNotExist:
            print("Error: El tipo de contratación no existe en la base de datos.")
        except Exception as e:
            print(f"Error al iniciar la contratación: {e}")
    
    def adjudicar_obra(self):
        """Adjudica la obra a una empresa"""
        try:
            empresa_nombre = input("Ingrese el nombre de la empresa: ")
            empresa_instance = Empresa.get(Empresa.nombre == empresa_nombre)
            
            nro_expediente = input("Ingrese el número de expediente: ")
            self.obra.empresa = empresa_instance
            self.obra.nro_expediente = nro_expediente
            self.obra.save()
            print(f"Obra '{self.obra.nombre}' adjudicada a la empresa '{empresa_nombre}'.")
        except peewee.DoesNotExist:
            print("Error: La empresa no existe en la base de datos.")
        except Exception as e:
            print(f"Error al adjudicar la obra: {e}")
    
    def iniciar_obra(self):
        """Inicia la obra asignando fecha de inicio y otros detalles"""
        try:
            self.obra.fecha_inicio = input("Ingrese la fecha de inicio de la obra (YYYY-MM-DD): ")
            self.obra.fecha_inicio = datetime.strptime(self.obra.fecha_inicio, "%Y-%m-%d")

            self.obra.fecha_fin_inicial = input("Ingrese la fecha de finalización inicial (YYYY-MM-DD): ")
            self.obra.fecha_fin_inicial = datetime.strptime(self.obra.fecha_fin_inicial, "%Y-%m-%d")

            fuente_financiamiento = input("Ingrese la fuente de financiamiento: ")
            fuente_financiamiento_instance = FuenteFinanciamiento.get(FuenteFinanciamiento.nombre == fuente_financiamiento)
            
            mano_obra = int(input("Ingrese la cantidad de mano de obra: "))
            self.obra.fuente_financiamiento = fuente_financiamiento_instance
            self.obra.mano_obra = mano_obra
            self.obra.save()
            print(f"Obra '{self.obra.nombre}' iniciada con fecha de inicio {self.obra.fecha_inicio}.")
        except peewee.DoesNotExist:
            print("Error: La fuente de financiamiento no existe en la base de datos.")
        except ValueError:
            print("Error: El formato de la fecha no es válido.")
        except Exception as e:
            print(f"Error al iniciar la obra: {e}")
    
    def actualizar_porcentaje_avance(self):
        """Actualiza el porcentaje de avance de la obra"""
        try:
            nuevo_avance = float(input("Ingrese el porcentaje de avance (0-100): "))
            if 0 <= nuevo_avance <= 100:
                self.obra.porcentaje_avance = nuevo_avance
                self.obra.save()
                print(f"Porcentaje de avance de la obra '{self.obra.nombre}' actualizado a {nuevo_avance}%.")
            else:
                print("Error: El porcentaje de avance debe estar entre 0 y 100.")
        except ValueError:
            print("Error: El valor ingresado no es válido.")
        except Exception as e:
            print(f"Error al actualizar el porcentaje de avance: {e}")
    
    def incrementar_plazo(self):
        """Incrementa el plazo de la obra"""
        try:
            incremento_plazo = int(input("Ingrese el número de meses para incrementar el plazo: "))
            self.obra.plazo_meses += incremento_plazo
            self.obra.save()
            print(f"Plazo de la obra '{self.obra.nombre}' incrementado en {incremento_plazo} meses.")
        except ValueError:
            print("Error: El valor ingresado no es válido.")
        except Exception as e:
            print(f"Error al incrementar el plazo de la obra: {e}")
    
    def incrementar_mano_obra(self):
        """Incrementa la cantidad de mano de obra de la obra"""
        try:
            incremento_mano_obra = int(input("Ingrese la cantidad de mano de obra a incrementar: "))
            self.obra.mano_obra += incremento_mano_obra
            self.obra.save()
            print(f"Mano de obra de la obra '{self.obra.nombre}' incrementada en {incremento_mano_obra} trabajadores.")
        except ValueError:
            print("Error: El valor ingresado no es válido.")
        except Exception as e:
            print(f"Error al incrementar la mano de obra: {e}")
    
    def finalizar_obra(self):
        """Finaliza la obra, estableciendo su etapa y porcentaje de avance"""
        try:
            self.obra.etapa = Etapa.get(Etapa.nombre == "Finalizada")
            self.obra.porcentaje_avance = 100
            self.obra.save()
            print(f"Obra '{self.obra.nombre}' finalizada con éxito.")
        except peewee.DoesNotExist:
            print("Error: La etapa 'Finalizada' no existe en la base de datos.")
        except Exception as e:
            print(f"Error al finalizar la obra: {e}")
    
    def rescindir_obra(self):
        """Rescinde la obra, cambiando su etapa a 'Rescindida'"""
        try:
            self.obra.etapa = Etapa.get(Etapa.nombre == "Rescindida")
            self.obra.save()
            print(f"Obra '{self.obra.nombre}' rescindida.")
        except peewee.DoesNotExist:
            print("Error: La etapa 'Rescindida' no existe en la base de datos.")
        except Exception as e:
            print(f"Error al rescindir la obra: {e}")