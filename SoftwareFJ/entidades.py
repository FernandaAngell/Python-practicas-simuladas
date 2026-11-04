from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador):
        self.__identificador = identificador

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def obtener_informacion(self):
        pass