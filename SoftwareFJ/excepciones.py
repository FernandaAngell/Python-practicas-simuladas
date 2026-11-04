class ErrorSistema(Exception):
    """Excepcion base del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error en los datos ingresados."""
    pass


class ErrorReserva(ErrorSistema):
    """Error al gestionar una reserva."""
    pass


class ServicioNoDisponible(ErrorSistema):
    """Servicio no disponible."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con un cliente."""
    pass