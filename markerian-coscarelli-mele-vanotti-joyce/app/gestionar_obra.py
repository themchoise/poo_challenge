from abc import ABC, abstractmethod
from datetime import datetime
from .obra import Obra


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

    @abstractmethod
    def obtener_indicadores(self):
        pass

    @abstractmethod
    def obtener_coordenadas(self):
        pass

    @classmethod
    def nueva_obra(self):
        return Obra()

