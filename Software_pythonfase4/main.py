# Importamos la clase encargada de construir la interfaz grafica.
from interfaz import InterfazSoftwareFJ

# Importamos la biblioteca tkinter para crear la ventana principal.
import tkinter as tk


# Funcion principal que inicia la aplicacion Software FJ.
def main():

    # Creamos la ventana principal de la aplicacion.
    ventana = tk.Tk()

    # Creamos una instancia de la interfaz y le enviamos la ventana.
    aplicacion = InterfazSoftwareFJ(
        ventana
    )

    # Iniciamos el ciclo principal de tkinter.
    # Esto permite mantener abierta la ventana y responder
    # a las acciones realizadas por el usuario.
    ventana.mainloop()


# Verificamos que este archivo se este ejecutando directamente.
# Si es asi, llamamos a la funcion principal.
if __name__ == "__main__":
    main()
