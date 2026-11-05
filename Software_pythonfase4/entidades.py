from abc import ABC, abstractmethod  # Importa las clases ABC y el decorador abstractmethod para crear clases abstractas


class Entidad(ABC):     # Define la clase abstracta Entidad que hereda de ABC

    def __init__(self, identificador):          # Método constructor que recibe un identificador único
        self.__identificador = identificador      # Almacena el identificador de forma privada (encapsulamiento)

    @property       # Define un decorador property para exponer el identificador de solo lectura
    def identificador(self):    # Método getter para obtener el valor del identificador protegido
        return self.__identificador      # Retorna el valor del identificador privado

    @abstractmethod   # Decorador que obliga a las clases hijas a implementar este método obligatoriamente
    def obtener_informacion(self):  # Firma abstracta del método para retornar la información de la entidad
        pass   # No tiene cuerpo aquí porque la implementación real se realiza en las clases hijas