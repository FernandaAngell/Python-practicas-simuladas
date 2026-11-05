class ErrorSistema(Exception):   # Define la clase base de excepción personalizada para el sistema[cite: 31]
    """Excepcion base del sistema."""   # Docstring descriptivo de la excepción base[cite: 31]
    pass   # Indica que la clase no añade atributos ni métodos adicionales[cite: 31]


class ErrorValidacion(ErrorSistema):   # Excepción para manejar errores en la validación de datos[cite: 31]
    """Error en los datos ingresados."""  # Docstring descriptivo del error de validación[cite: 31]
    pass  # Hereda todo el comportamiento de ErrorSistema sin agregar miembros[cite: 31]


class ErrorReserva(ErrorSistema):  # Excepción específica para fallos relacionados con reservas[cite: 31]
    """Error al gestionar una reserva."""    # Docstring que describe el error en la gestión de reservas[cite: 31]
    pass  # Mantiene la implementación limpia heredando de ErrorSistema[cite: 31]


class ServicioNoDisponible(ErrorSistema):  # Excepción cuando un servicio no está disponible o falla[cite: 31]
    """Servicio no disponible."""  # Docstring para identificar indisponibilidad de servicio[cite: 31]
    pass  # Hereda de ErrorSistema sin modificaciones[cite: 31]


class ErrorCliente(ErrorSistema):  # Excepción para anomalías relacionadas con la entidad cliente[cite: 31]
    """Error relacionado con un cliente."""  # Docstring que aclara el uso de este error[cite: 31]
    pass  # Implementación mínima basada en ErrorSistema[cite: 31]