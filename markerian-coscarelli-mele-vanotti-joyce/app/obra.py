from datetime import datetime
import peewee
from app.models import Etapa, ContratacionTipo, Licitacion_oferta_empresa, Financiamiento
from peewee import *
from app.helpers.buscar_registro import buscar_registro
from app.modelo_obra import GestionObraModel

class Obra:
    
    def __init__(self, obra_instance:GestionObraModel):
        self.obra = obra_instance  # 

    def nuevo_proyecto(self):
        """Inicia un nuevo proyecto de obra"""
        try:
            etapa_proyecto, creado = Etapa.get_or_create(etapa="Proyecto")
            self.obra.etapa = etapa_proyecto.id  
            self.obra.save()
        
            print(f"Obra '{self.obra.nombre}' iniciada como Proyecto.")
        except Exception as e:
            print(f"Error al iniciar el proyecto: {e}")

    def iniciar_contratacion(self):
        try:
            contratacion_tipo_input = input("Ingrese el tipo de contratación, ejemplo (Contratación Directa): ")
            registro_db_tipo_contratacion = buscar_registro(contratacion_tipo_input, ContratacionTipo,'contratacion_tipo')
            
            nro_contratacion = input("Ingrese el número de contratación: ")
            self.obra.contratacion_tipo = registro_db_tipo_contratacion
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
            empresa_nombre_input = input("Ingrese el nombre de la empresa, ejemplo(SES SA): ")

            registro_db_empresa = buscar_registro(empresa_nombre_input,Licitacion_oferta_empresa,'licitacion_oferta_empresa')
            self.obra.licitacion_oferta_empresa = registro_db_empresa

            expediente_numero_input = input("Ingrese el número de expediente: ")
                        
            self.obra.expediente_numero = expediente_numero_input
            self.obra.save()
            print("Adjudicacion Finalizada")
        except peewee.DoesNotExist:
            print("Error: La empresa no existe en la base de datos.")
        except Exception as e:
            print(f"Error al adjudicar la obra: {e}")
    
    def iniciar_obra(self):
        """Inicia la obra asignando fecha de inicio y otros detalles"""
        try:
            self.obra.fecha_inicio = input("Ingrese la fecha de inicio de la obra (YYYY-MM-DD): ")
            self.obra.fecha_fin_inicial = input("Ingrese la fecha de finalización inicial (YYYY-MM-DD): ")
            mano_obra = int(input("Ingrese la cantidad de mano de obra: "))            
            fuente_financiamiento_input = input("Ingrese la fuente de financiamiento: ")

            registro_db_financiamiento = buscar_registro(fuente_financiamiento_input,Financiamiento,'financiamiento')
            
            self.obra.fecha_fin_inicial = datetime.strptime(self.obra.fecha_fin_inicial, "%Y-%m-%d")
            self.obra.fecha_inicio = datetime.strptime(self.obra.fecha_inicio, "%Y-%m-%d")
            self.obra.financiamiento = registro_db_financiamiento
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

        try:
            incremento_plazo = int(input("Ingrese el número de meses para incrementar el plazo: "))
            plazo_meses_actual = 0 if self.obra.plazo_meses is None else self.obra.plazo_meses
            self.obra.plazo_meses = plazo_meses_actual+ incremento_plazo
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
            self.obra.etapa = Etapa.get(Etapa.etapa == "Finalizada")
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
            self.obra.etapa = Etapa.get(Etapa.etapa == "Rescisión")
            self.obra.save()
            print(f"Obra '{self.obra.nombre}' rescindida.")
        except peewee.DoesNotExist:
            print("Error: La etapa 'Rescisión' no existe en la base de datos.")
        except Exception as e:
            print(f"Error al rescindir la obra: {e}")