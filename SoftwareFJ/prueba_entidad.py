
from entidades import Entidad


class ClientePrueba(Entidad):

    def obtener_informacion(self):
        return f"Cliente: {self.identificador}"


cliente = ClientePrueba(1)

print(cliente.obtener_informacion())
