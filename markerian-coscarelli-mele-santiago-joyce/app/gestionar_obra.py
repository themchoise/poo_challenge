from abc import ABC, abstractmethod
from datetime import datetime



class GestionarObra(ABC):


    @abstractmethod
    def extraer_datos(self):
        pass

    @abstractmethod
    def conectar_db(self):
        pass

    @abstractmethod
    def mapear_orm(self):
        pass

    @abstractmethod
    def limpiar_datos(self):
        pass

    @abstractmethod
    def cargar_datos(self):
        pass

    @abstractmethod
    def nueva_obra(self):
        pass

    @classmethod
    def nueva_obra(self):
        pass

