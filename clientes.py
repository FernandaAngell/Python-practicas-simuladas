
# Importamos la clase abstracta Entidad para heredar
# sus atributos y metodos.
from entidades import Entidad

# Importamos la excepcion personalizada para controlar
# los errores relacionados con los datos del cliente.
from excepciones import ErrorValidacion


# Creamos la clase Cliente, que hereda de Entidad.
class Cliente(Entidad):

    # Constructor de la clase.
    # Recibe el identificador, nombre, correo y telefono.
    def __init__(self, identificador, nombre, correo, telefono):

        # Llamamos al constructor de la clase padre
        # para inicializar el identificador.
        super().__init__(identificador)

        # Validamos que el nombre no este vacio.
        if not nombre.strip():
            raise ErrorValidacion("El nombre es obligatorio.")

        # Validamos que el correo tenga un formato basico.
        if "@" not in correo or "." not in correo:
            raise ErrorValidacion("Correo electronico invalido.")

        # Validamos que el telefono contenga solo numeros
        # y tenga como minimo siete digitos.
        if not telefono.isdigit() or len(telefono) < 7:
            raise ErrorValidacion("Telefono invalido.")

        # Encapsulamos los datos personales del cliente
        # utilizando atributos privados.
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Propiedad para consultar el nombre del cliente.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el correo electronico.
    @property
    def correo(self):
        return self.__correo

    # Propiedad para consultar el telefono.
    @property
    def telefono(self):
        return self.__telefono

    # Implementamos el metodo abstracto heredado de Entidad.
    # Retorna la informacion general del cliente.
    def obtener_informacion(self):
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )
