from excepciones import ErrorReserva


class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion):
        if duracion <= 0:
            raise ErrorReserva("Duracion invalida.")

        self.identificador = identificador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def calcular_costo(self, descuento=0, impuesto=0):
        costo = self.servicio.calcular_costo(self.duracion)

        if descuento < 0 or descuento > 100:
            raise ErrorReserva("Descuento invalido.")

        if impuesto < 0:
            raise ErrorReserva("Impuesto invalido.")

        costo -= costo * descuento / 100
        costo += costo * impuesto / 100

        return costo

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.estado = "Confirmada"

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya esta cancelada.")

        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.calcular_costo()
            self.confirmar()
            return costo

        except ErrorReserva:
            raise

        except Exception as error:
            raise ErrorReserva(
                "Error al procesar la reserva."
            ) from error

        finally:
            print(
                f"Procesamiento de reserva "
                f"{self.identificador} finalizado."
            )

    def obtener_informacion(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )