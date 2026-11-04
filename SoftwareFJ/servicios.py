from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


class Servicio(ABC):

    def __init__(self, identificador, nombre, precio):
        if precio <= 0:
            raise ErrorValidacion("El precio debe ser positivo.")

        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    def validar_duracion(self, duracion):
        if duracion <= 0:
            raise ErrorValidacion(
                "La duracion debe ser mayor que cero."
            )


class ReservaSala(Servicio):

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.precio * duracion

    def describir(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.precio * duracion

    def describir(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion):
        self.validar_duracion(duracion)
        return self.precio * duracion

    def describir(self):
        return f"Asesoria especializada: {self.nombre}"