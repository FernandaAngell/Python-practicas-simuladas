from entidades import Entidad
from excepciones import ErrorValidacion


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        if not nombre.strip():
            raise ErrorValidacion("El nombre es obligatorio.")

        if "@" not in correo or "." not in correo:
            raise ErrorValidacion("Correo electronico invalido.")

        if not telefono.isdigit() or len(telefono) < 7:
            raise ErrorValidacion("Telefono invalido.")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def obtener_informacion(self):
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )