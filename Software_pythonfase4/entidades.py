from abc import ABC, abstractmethod  # Importa las utilidades para definir clases y métodos abstractos[cite: 30]


class Entidad(ABC):     # Define la clase base abstracta Entidad[cite: 30]

    def __init__(self, identificador):            # Constructor de la clase que recibe el identificador único[cite: 30]
        self.__identificador = identificador      # Asigna el identificador a un atributo privado[cite: 30]

    @property       # Decorador para convertir el método identificador en una propiedad de solo lectura[cite: 30]
    def identificador(self):    # Getter para acceder al atributo privado del identificador[cite: 30]
        return self.__identificador      # Retorna el valor del atributo privado identificador[cite: 30]

    @abstractmethod   # Decorador que obliga a las clases hijas a implementar el método[cite: 30]
    def obtener_informacion(self):  # Método abstracto para obtener la información de la entidad[cite: 30]
        pass   # Declaración vacía que será sobrescrita en las clases derivadas[cite: 30]