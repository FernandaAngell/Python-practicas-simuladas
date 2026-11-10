# Importamos la excepción personalizada para manejar errores relacionados
# con las reservas.
from excepciones import ErrorReserva


# Clase que representa una reserva.
class Reserva:

    # Constructor de la clase.
    # Recibe un identificador, un cliente, un servicio y la duración.
    def __init__(self, identificador, cliente, servicio, duracion):

        # Validamos que la duración sea mayor que cero.
        if duracion <= 0:
            raise ErrorReserva("Duracion invalida.")

        # Guardamos los datos de la reserva.
        self.identificador = identificador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        # Toda reserva comienza inicialmente en estado "Pendiente".
        self.estado = "Pendiente"

    # Método encargado de calcular el costo total de la reserva.
    # Permite aplicar opcionalmente un descuento y un impuesto.
    def calcular_costo(self, descuento=0, impuesto=0):

        # Calculamos primero el costo del servicio según la duración.
        costo = self.servicio.calcular_costo(self.duracion)

        # Validamos que el descuento esté entre 0% y 100%.
        if descuento < 0 or descuento > 100:
            raise ErrorReserva("Descuento invalido.")

        # El impuesto no puede ser negativo.
        if impuesto < 0:
            raise ErrorReserva("Impuesto invalido.")

        # Aplicamos el descuento al costo.
        costo -= costo * descuento / 100

        # Después agregamos el impuesto al costo.
        costo += costo * impuesto / 100

        # Retornamos el costo final.
        return costo

    # Método para confirmar una reserva.
    def confirmar(self):

        # Solo se puede confirmar una reserva que esté pendiente.
        if self.estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        # Cambiamos el estado de la reserva a confirmada.
        self.estado = "Confirmada"

    # Método para cancelar una reserva.
    def cancelar(self):

        # Verificamos si la reserva ya estaba cancelada.
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya esta cancelada.")

        # Cambiamos el estado de la reserva a cancelada.
        self.estado = "Cancelada"

    # Método que se encarga de procesar la reserva.
    def procesar(self):

        # Iniciamos un bloque para controlar posibles errores.
        try:

            # Calculamos el costo de la reserva.
            costo = self.calcular_costo()

            # Si el cálculo es correcto, confirmamos la reserva.
            self.confirmar()

            # Retornamos el costo calculado.
            return costo

        # Si ocurre un error generado por nuestra clase ErrorReserva,
        # lo volvemos a lanzar sin modificarlo.
        except ErrorReserva:
            raise

        # Capturamos cualquier otro tipo de error inesperado.
        except Exception as error:

            # Convertimos el error en una excepción de tipo ErrorReserva.
            # "from error" conserva el error original como causa.
            raise ErrorReserva(
                "Error al procesar la reserva."
            ) from error

        # Este bloque siempre se ejecuta, haya ocurrido un error o no.
        finally:

            # Mostramos un mensaje indicando que terminó el procesamiento.
            print(
                f"Procesamiento de reserva "
                f"{self.identificador} finalizado."
            )

    # Método que devuelve la información principal de la reserva.
    def obtener_informacion(self):

        # Construimos y retornamos un texto con los datos de la reserva.
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
