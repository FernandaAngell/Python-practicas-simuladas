# Importo la librería nativa de Python para diseñar interfaces gráficas (Tkinter)
import tkinter as tk
# Importo los componentes extendidos de Tkinter (ttk) y la herramienta de cuadros de diálogo (messagebox)
from tkinter import ttk, messagebox
# Importo el módulo de Python para gestionar registros de eventos y logs del sistema
import logging
# Importo la clase base para la creación y gestión de clientes
from clientes import Cliente
# Importo las clases de servicios disponibles (reserva de salas, alquiler de equipos y asesorías)
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
# Importo la clase encargada de administrar el ciclo de vida y costos de las reservas
from reservas import Reserva

# Configuro los parámetros básicos del registro de eventos guardándolos en un archivo "sistema.log"
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Defino la clase principal que estructura y controla la interfaz gráfica del software
class InterfazSoftwareFJ:
# Método inicializador de la clase que configura la ventana principal y sus atributos
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software FJ - Gestion Integral")
        self.ventana.geometry("1000x650")
        self.ventana.minsize(850, 550)
# Inicializo las listas vacías para almacenar los objetos en memoria localmente
        self.clientes = []
        self.servicios = []
        self.reservas = []
# Invoco el método que dibuja la interfaz y sus pestañas principales
        self.crear_interfaz()
# Método para organizar los elementos visuales generales de la ventana principal
    def crear_interfaz(self):
# Creo la etiqueta gráfica que muestra el título principal del software
        titulo = tk.Label(
            self.ventana,
            text="SOFTWARE FJ",
            font=("Arial", 22, "bold"),
            fg="#1F4E79"
        )
        titulo.pack(pady=15)
# Creo una etiqueta subtítulo para describir la finalidad del sistema
        subtitulo = tk.Label(
            self.ventana,
            text="Sistema Integral de Clientes, Servicios y Reservas",
            font=("Arial", 12)
        )
        subtitulo.pack(pady=5)
# Configuro el componente de pestañas (Notebook) para segmentar las vistas del programa
        self.pestanas = ttk.Notebook(self.ventana)
        self.pestanas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
# Instancio un marco (frame) independiente para la sección de clientes
        self.pestana_clientes = ttk.Frame(self.pestanas)
        # Instancio un marco independiente para la sección de servicios
        self.pestana_servicios = ttk.Frame(self.pestanas)
        # Instancio un marco independiente para la sección de reservas
        self.pestana_reservas = ttk.Frame(self.pestanas)
# Añado la pestaña de clientes al contenedor de pestañas con su respectiva etiqueta
        self.pestanas.add(
            self.pestana_clientes,
            text="Clientes"
        )
# Añado la pestaña de servicios al contenedor principal
        self.pestanas.add(
            self.pestana_servicios,
            text="Servicios"
        )
# Añado la pestaña de reservas al contenedor principal
        self.pestanas.add(
            self.pestana_reservas,
            text="Reservas"
        )
# Llamo a la función que construye el contenido visual de la pestaña de clientes
        self.crear_pestana_clientes()
        # Llamo a la función que construye el contenido visual de la pestaña de servicios
        self.crear_pestana_servicios()
        # Llamo a la función que construye el contenido visual de la pestaña de reservas
        self.crear_pestana_reservas()

    # ---------------- CLIENTES ----------------
# Método que diseña los componentes gráficos de la pestaña de gestión de clientes
    def crear_pestana_clientes(self):
# Creo un marco enmarcado para agrupar los campos del formulario de registro de clientes
        formulario = ttk.LabelFrame(
            self.pestana_clientes,
            text="Registrar Cliente"
        )
        formulario.pack(fill="x", padx=15, pady=15)
# Etiqueta estática para indicar el campo de texto del nombre
        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=0, column=0, padx=10, pady=10)
# Campo de entrada (Entry) para digitar el nombre del cliente
        self.nombre_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.nombre_cliente.grid(row=0, column=1, padx=10)
# Etiqueta estática para indicar el campo de correo electrónico
        ttk.Label(
            formulario,
            text="Correo:"
        ).grid(row=1, column=0, padx=10, pady=10)
# Campo de entrada para digitar el correo electrónico del cliente
        self.correo_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.correo_cliente.grid(row=1, column=1, padx=10)
# Etiqueta estática para el número telefónico
        ttk.Label(
            formulario,
            text="Telefono:"
        ).grid(row=2, column=0, padx=10, pady=10)
# Campo de entrada para digitar el teléfono del cliente
        self.telefono_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.telefono_cliente.grid(row=2, column=1, padx=10)
# Botón interactivo que ejecuta la acción de guardar el cliente ingresado
        ttk.Button(
            formulario,
            text="Registrar Cliente",
            command=self.registrar_cliente
        ).grid(row=3, column=0, columnspan=2, pady=15)
# Tabla (Treeview) para mostrar en forma de lista los clientes registrados en el sistema
        self.tabla_clientes = ttk.Treeview(
            self.pestana_clientes,
            columns=("ID", "Nombre", "Correo", "Telefono"),
            show="headings"
        )
# Bucle para configurar los títulos y el ancho de cada columna de la tabla de clientes
        for columna in (
            "ID",
            "Nombre",
            "Correo",
            "Telefono"
        ):
            self.tabla_clientes.heading(
                columna,
                text=columna
            )

            self.tabla_clientes.column(
                columna,
                width=150
            )
# Posiciono y configuro la expansión visual de la tabla dentro de su pestaña
        self.tabla_clientes.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )
# Método que procesa la lógica cuando el usuario intenta registrar un nuevo cliente
    def registrar_cliente(self):

        try:
            # Capturo el texto ingresado en el campo nombre eliminando espacios vacíos en los extremos
            nombre = self.nombre_cliente.get().strip()
            # Capturo el texto ingresado en el campo correo eliminando espacios sobrantes
            correo = self.correo_cliente.get().strip()
            # Capturo el texto ingresado en el campo teléfono eliminando espacios sobrantes
            telefono = self.telefono_cliente.get().strip()
# Asigno un identificador numérico automático basado en el total actual de clientes
            identificador = len(self.clientes) + 1
# Instancio un nuevo objeto de tipo Cliente con los datos recolectados
            cliente = Cliente(
                identificador,
                nombre,
                correo,
                telefono
            )
# Agrego el cliente creado a la lista temporal almacenada en memoria
            self.clientes.append(cliente)
# Inserto una nueva fila en la tabla visual con la información del cliente
            self.tabla_clientes.insert(
                "",
                "end",
                values=(
                    cliente.identificador,
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono
                )
            )
# Registro un evento informativo en el archivo de logs del sistema
            logging.info(
                f"Cliente registrado: {cliente.nombre}"
            )
# Despliego un cuadro de diálogo informando al usuario que el registro fue exitoso
            messagebox.showinfo(
                "Registro exitoso",
                "El cliente fue registrado correctamente."
            )
# Borro el contenido de la caja de texto del nombre para dejarla limpia
            self.nombre_cliente.delete(0, tk.END)
            # Borro el contenido de la caja de texto del correo
            self.correo_cliente.delete(0, tk.END)
            # Borro el contenido de la caja de texto del teléfono
            self.telefono_cliente.delete(0, tk.END)
# Actualizo el selector desplegable de clientes disponible en la pestaña de reservas
            self.actualizar_clientes_reserva()

        except Exception as error:
# Capturo cualquier excepción o error de validación y lo guardo en el archivo de registro
            logging.exception(
                "Error al registrar cliente"
            )
# Muestro una ventana emergente indicando el error exacto ocurrido
            messagebox.showerror(
                "Error",
                str(error)
            )

    # ---------------- SERVICIOS ----------------

    def crear_pestana_servicios(self):

        formulario = ttk.LabelFrame(
            self.pestana_servicios,
            text="Crear Servicio"
        )
        formulario.pack(fill="x", padx=15, pady=15)

        ttk.Label(
            formulario,
            text="Tipo de servicio:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.tipo_servicio = ttk.Combobox(
            formulario,
            values=[
                "Reserva de sala",
                "Alquiler de equipo",
                "Asesoria especializada"
            ],
            state="readonly"
        )

        self.tipo_servicio.grid(
            row=0,
            column=1,
            padx=10
        )

        self.tipo_servicio.current(0)

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.nombre_servicio = ttk.Entry(
            formulario,
            width=30
        )
        self.nombre_servicio.grid(
            row=1,
            column=1,
            padx=10
        )

        ttk.Label(
            formulario,
            text="Precio por unidad:"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.precio_servicio = ttk.Entry(
            formulario,
            width=30
        )
        self.precio_servicio.grid(
            row=2,
            column=1,
            padx=10
        )

        ttk.Button(
            formulario,
            text="Crear Servicio",
            command=self.crear_servicio
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=15
        )

        self.tabla_servicios = ttk.Treeview(
            self.pestana_servicios,
            columns=("ID", "Tipo", "Nombre", "Precio"),
            show="headings"
        )

        for columna in (
            "ID",
            "Tipo",
            "Nombre",
            "Precio"
        ):
            self.tabla_servicios.heading(
                columna,
                text=columna
            )

            self.tabla_servicios.column(
                columna,
                width=150
            )

        self.tabla_servicios.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

    def crear_servicio(self):

        try:
            tipo = self.tipo_servicio.get()
            nombre = self.nombre_servicio.get().strip()
            precio = float(self.precio_servicio.get())

            identificador = len(self.servicios) + 1

            if tipo == "Reserva de sala":

                servicio = ReservaSala(
                    identificador,
                    nombre,
                    precio
                )

            elif tipo == "Alquiler de equipo":

                servicio = AlquilerEquipo(
                    identificador,
                    nombre,
                    precio
                )

            else:

                servicio = AsesoriaEspecializada(
                    identificador,
                    nombre,
                    precio
                )

            self.servicios.append(servicio)

            self.tabla_servicios.insert(
                "",
                "end",
                values=(
                    servicio.identificador,
                    tipo,
                    servicio.nombre,
                    f"${servicio.precio:,.2f}"
                )
            )

            logging.info(
                f"Servicio creado: {servicio.nombre}"
            )

            messagebox.showinfo(
                "Servicio creado",
                "El servicio fue creado correctamente."
            )

            self.nombre_servicio.delete(0, tk.END)
            self.precio_servicio.delete(0, tk.END)

            self.actualizar_servicios_reserva()

        except Exception as error:

            logging.exception(
                "Error al crear servicio"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ---------------- RESERVAS ----------------

    def crear_pestana_reservas(self):

        formulario = ttk.LabelFrame(
            self.pestana_reservas,
            text="Crear Reserva"
        )
        formulario.pack(fill="x", padx=15, pady=15)

        ttk.Label(
            formulario,
            text="Cliente:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.cliente_reserva = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.cliente_reserva.grid(
            row=0,
            column=1,
            padx=10
        )

        ttk.Label(
            formulario,
            text="Servicio:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.servicio_reserva = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.servicio_reserva.grid(
            row=1,
            column=1,
            padx=10
        )

        ttk.Label(
            formulario,
            text="Duracion:"
        ).grid(row=2, column=0, padx=10, pady=10)

        self.duracion_reserva = ttk.Entry(
            formulario,
            width=35
        )

        self.duracion_reserva.grid(
            row=2,
            column=1,
            padx=10
        )

        ttk.Button(
            formulario,
            text="Crear Reserva",
            command=self.crear_reserva
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=15
        )

        self.tabla_reservas = ttk.Treeview(
            self.pestana_reservas,
            columns=(
                "ID",
                "Cliente",
                "Servicio",
                "Duracion",
                "Estado",
                "Costo"
            ),
            show="headings"
        )

        for columna in (
            "ID",
            "Cliente",
            "Servicio",
            "Duracion",
            "Estado",
            "Costo"
        ):
            self.tabla_reservas.heading(
                columna,
                text=columna
            )

            self.tabla_reservas.column(
                columna,
                width=130
            )

        self.tabla_reservas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        botones = ttk.Frame(
            self.pestana_reservas
        )

        botones.pack(pady=10)

        ttk.Button(
            botones,
            text="Confirmar Reserva",
            command=self.confirmar_reserva
        ).pack(side="left", padx=5)

        ttk.Button(
            botones,
            text="Cancelar Reserva",
            command=self.cancelar_reserva
        ).pack(side="left", padx=5)

    def actualizar_clientes_reserva(self):

        self.cliente_reserva["values"] = [
            f"{cliente.identificador} - {cliente.nombre}"
            for cliente in self.clientes
        ]

    def actualizar_servicios_reserva(self):

        self.servicio_reserva["values"] = [
            f"{servicio.identificador} - {servicio.nombre}"
            for servicio in self.servicios
        ]

    def crear_reserva(self):

        try:
            cliente_seleccionado = (
                self.cliente_reserva.get()
            )

            servicio_seleccionado = (
                self.servicio_reserva.get()
            )

            if not cliente_seleccionado:
                raise ValueError(
                    "Debe seleccionar un cliente."
                )

            if not servicio_seleccionado:
                raise ValueError(
                    "Debe seleccionar un servicio."
                )

            duracion = int(
                self.duracion_reserva.get()
            )

            cliente_id = int(
                cliente_seleccionado.split(" - ")[0]
            )

            servicio_id = int(
                servicio_seleccionado.split(" - ")[0]
            )

            cliente = next(
                c for c in self.clientes
                if c.identificador == cliente_id
            )

            servicio = next(
                s for s in self.servicios
                if s.identificador == servicio_id
            )

            identificador = len(self.reservas) + 1

            reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            costo = reserva.calcular_costo()

            self.reservas.append(reserva)

            self.tabla_reservas.insert(
                "",
                "end",
                iid=str(identificador),
                values=(
                    identificador,
                    cliente.nombre,
                    servicio.nombre,
                    duracion,
                    reserva.estado,
                    f"${costo:,.2f}"
                )
            )

            logging.info(
                f"Reserva creada: {identificador}"
            )

            messagebox.showinfo(
                "Reserva creada",
                f"Reserva creada correctamente.\n"
                f"Costo: ${costo:,.2f}"
            )

            self.duracion_reserva.delete(
                0,
                tk.END
            )

        except Exception as error:

            logging.exception(
                "Error al crear reserva"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

    def confirmar_reserva(self):

        seleccion = (
            self.tabla_reservas.selection()
        )

        if not seleccion:
            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva."
            )
            return

        try:
            identificador = int(seleccion[0])

            reserva = next(
                r for r in self.reservas
                if r.identificador == identificador
            )

            reserva.confirmar()

            self.actualizar_tabla_reserva(
                reserva
            )

            logging.info(
                f"Reserva confirmada: {identificador}"
            )

            messagebox.showinfo(
                "Reserva",
                "Reserva confirmada correctamente."
            )

        except Exception as error:

            logging.exception(
                "Error al confirmar reserva"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

    def cancelar_reserva(self):

        seleccion = (
            self.tabla_reservas.selection()
        )

        if not seleccion:
            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva."
            )
            return

        try:
            identificador = int(seleccion[0])

            reserva = next(
                r for r in self.reservas
                if r.identificador == identificador
            )

            reserva.cancelar()

            self.actualizar_tabla_reserva(
                reserva
            )

            logging.info(
                f"Reserva cancelada: {identificador}"
            )

            messagebox.showinfo(
                "Reserva",
                "Reserva cancelada correctamente."
            )

        except Exception as error:

            logging.exception(
                "Error al cancelar reserva"
            )

            messagebox.showerror(
                "Error",
                str(error)
            )

    def actualizar_tabla_reserva(self, reserva):

        costo = reserva.calcular_costo()

        self.tabla_reservas.item(
            str(reserva.identificador),
            values=(
                reserva.identificador,
                reserva.cliente.nombre,
                reserva.servicio.nombre,
                reserva.duracion,
                reserva.estado,
                f"${costo:,.2f}"
            )
        )


if __name__ == "__main__":

    ventana = tk.Tk()

    aplicacion = InterfazSoftwareFJ(
        ventana
    )

    ventana.mainloop()
