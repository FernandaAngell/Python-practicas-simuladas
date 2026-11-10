# Importamos ABC y abstractmethod para poder crear una clase abstracta
# y definir métodos que las clases hijas deben implementar.
from abc import ABC, abstractmethod

# Importamos nuestra excepción personalizada para validar errores.
from excepciones import ErrorValidacion


# Clase abstracta que representa un servicio.
# ABC indica que esta clase no está pensada para crear objetos directamente.
class Servicio(ABC):

    # Constructor de la clase.
    # Recibe un identificador, un nombre y un precio.
    def __init__(self, identificador, nombre, precio):

        # Validamos que el precio sea mayor que cero.
        if precio <= 0:
            raise ErrorValidacion("El precio debe ser positivo.")

        # Guardamos los datos del servicio.
        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio

    # Método abstracto para calcular el costo.
    # Las clases hijas están obligadas a implementarlo.
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Método abstracto para describir el servicio.
    # Cada clase hija debe proporcionar su propia descripción.
    @abstractmethod
    def describir(self):
        pass

    # Método para validar que la duración sea correcta.
    def validar_duracion(self, duracion):

        # La duración debe ser mayor que cero.
        if duracion <= 0:
            raise ErrorValidacion(
                "La duracion debe ser mayor que cero."
            )


# Clase hija que representa una reserva de sala.
# Hereda los atributos y métodos de Servicio.
class ReservaSala(Servicio):

    # Calcula el costo multiplicando el precio por la duración.
    def calcular_costo(self, duracion):

        # Primero validamos que la duración sea válida.
        self.validar_duracion(duracion)

        # Retornamos el costo total.
        return self.precio * duracion

    # Devuelve una descripción específica para una reserva de sala.
    def describir(self):
        return f"Reserva de sala: {self.nombre}"


# Clase hija que representa el alquiler de un equipo.
class AlquilerEquipo(Servicio):

    # Calcula el costo del alquiler según la duración.
    def calcular_costo(self, duracion):

        # Validamos la duración.
        self.validar_duracion(duracion)

        # Calculamos y retornamos el costo total.
        return self.precio * duracion

    # Devuelve una descripción específica del equipo alquilado.
    def describir(self):
        return f"Alquiler de equipo: {self.nombre}"


# Clase hija que representa una asesoría especializada.
class AsesoriaEspecializada(Servicio):

    # Calcula el costo de la asesoría según su duración.
    def calcular_costo(self, duracion):

        # Validamos que la duración sea mayor que cero.
        self.validar_duracion(duracion)

        # Calculamos el costo total.
        return self.precio * duracion

    # Devuelve una descripción específica de la asesoría.
    def describir(self):
        return f"Asesoria especializada: {self.nombre}"
