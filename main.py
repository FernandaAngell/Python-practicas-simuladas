
from interfaz import InterfazSoftwareFJ
import tkinter as tk


def main():

    ventana = tk.Tk()

    aplicacion = InterfazSoftwareFJ(
        ventana
    )

    ventana.mainloop()


if __name__ == "__main__":
    main()
