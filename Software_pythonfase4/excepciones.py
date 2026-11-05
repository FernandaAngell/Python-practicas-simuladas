class ErrorSistema(Exception):   # Define la clase base de excepción personalizada para el sistema
    """Excepcion base del sistema."""   # Docstring descriptivo de la excepción base
    pass   # Indica que la clase no añade atributos ni métodos adicionales


class ErrorValidacion(ErrorSistema):   # Excepción para manejar errores en la validación de datos
    """Error en los datos ingresados."""  # Docstring descriptivo del error de validación
    pass  # Hereda todo el comportamiento de ErrorSistema sin agregar miembros


class ErrorReserva(ErrorSistema):  # Excepción específica para fallos relacionados con reservas
    """Error al gestionar una reserva."""    # Docstring que describe el error en la gestión de reservas
    pass  # Mantiene la implementación limpia heredando de ErrorSistema


class ServicioNoDisponible(ErrorSistema):  # Excepción cuando un servicio no está disponible o falla
    """Servicio no disponible."""  # Docstring para identificar indisponibilidad de servicio
    pass  # Hereda de ErrorSistema sin modificaciones


class ErrorCliente(ErrorSistema):  # Excepción para anomalías relacionadas con la entidad cliente
    """Error relacionado con un cliente."""  # Docstring que aclara el uso de este error
    pass  # Implementación mínima basada en ErrorSistema