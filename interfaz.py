## Código cometando por los 3 integrantes del grupo...﻿
# Importa Tkinter para construir la ventana y los controles gráficos.
import tkinter as tk
# Importa widgets adicionales y cuadros de diálogo para mostrar mensajes.
from tkinter import ttk, messagebox
# Importa logging para registrar eventos y errores del programa.
import logging

# Importa la clase Cliente, utilizada para crear y gestionar clientes.
from clientes import Cliente
# Importa las clases concretas de los servicios disponibles.
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
# Importa la clase Reserva para crear y administrar reservas.
from reservas import Reserva


# Configura el sistema de registro de eventos.
logging.basicConfig(
# Indica que los registros se guardarán en el archivo sistema.log.
    filename="sistema.log",
# Define INFO como el nivel mínimo de mensajes que se guardarán.
    level=logging.INFO,
# Define el formato de cada registro: fecha, nivel y mensaje.
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Declara la clase que reúne la interfaz gráfica de Software FJ.
class InterfazSoftwareFJ:

# Constructor de la clase: recibe la ventana principal.
    def __init__(self, ventana):
# Guarda la referencia a la ventana para configurarla desde otros métodos.
        self.ventana = ventana
# Establece el texto que aparece en la barra de título.
        self.ventana.title("Software FJ - Gestion Integral")
# Define el tamaño inicial de la ventana.
        self.ventana.geometry("1000x650")
# Establece el tamaño mínimo permitido para la ventana.
        self.ventana.minsize(850, 550)

# Lista en memoria donde se guardan los objetos Cliente.
        self.clientes = []
# Lista en memoria donde se guardan los objetos de servicio.
        self.servicios = []
# Lista en memoria donde se guardan los objetos Reserva.
        self.reservas = []

# Construye los componentes visuales de la aplicación.
        self.crear_interfaz()

# Organiza los elementos generales que aparecen en la ventana.
    def crear_interfaz(self):

# Crea el título principal de la aplicación.
        titulo = tk.Label(
            self.ventana,
            text="SOFTWARE FJ",
            font=("Arial", 22, "bold"),
            fg="#1F4E79"
        )
# Coloca el título en la ventana y agrega espacio vertical.
        titulo.pack(pady=15)

# Crea el subtítulo que describe el propósito del sistema.
        subtitulo = tk.Label(
            self.ventana,
            text="Sistema Integral de Clientes, Servicios y Reservas",
            font=("Arial", 12)
        )
# Coloca el subtítulo debajo del título principal.
        subtitulo.pack(pady=5)

# Crea un control Notebook para organizar la interfaz en pestañas.
        self.pestanas = ttk.Notebook(self.ventana)
# Configura el Notebook para ocupar el espacio disponible.
        self.pestanas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

# Crea el panel que contendrá los controles de clientes.
        self.pestana_clientes = ttk.Frame(self.pestanas)
# Crea el panel que contendrá los controles de servicios.
        self.pestana_servicios = ttk.Frame(self.pestanas)
# Crea el panel que contendrá los controles de reservas.
        self.pestana_reservas = ttk.Frame(self.pestanas)

# Agrega el panel de clientes al Notebook y nombra su pestaña.
        self.pestanas.add(
            self.pestana_clientes,
            text="Clientes"
        )

# Agrega el panel de servicios y define el texto de su pestaña.
        self.pestanas.add(
            self.pestana_servicios,
            text="Servicios"
        )

# Agrega el panel de reservas y define el texto de su pestaña.
        self.pestanas.add(
            self.pestana_reservas,
            text="Reservas"
        )

# Construye el formulario y la tabla de la sección de clientes.
        self.crear_pestana_clientes()
# Construye el formulario y la tabla de la sección de servicios.
        self.crear_pestana_servicios()
# Construye el formulario y la tabla de la sección de reservas.
        self.crear_pestana_reservas()

    # ---------------- CLIENTES ----------------

# Define los elementos visuales de la pestaña Clientes.
    def crear_pestana_clientes(self):

# Crea un recuadro que agrupa los campos del formulario.
        formulario = ttk.LabelFrame(
            self.pestana_clientes,
            text="Registrar Cliente"
        )
        formulario.pack(fill="x", padx=15, pady=15)

# Muestra la etiqueta que identifica el campo del nombre.
        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=0, column=0, padx=10, pady=10)

# Crea el campo de entrada para escribir el nombre del cliente.
        self.nombre_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.nombre_cliente.grid(row=0, column=1, padx=10)

# Muestra la etiqueta del campo de correo electrónico.
        ttk.Label(
            formulario,
            text="Correo:"
        ).grid(row=1, column=0, padx=10, pady=10)

# Crea el campo de entrada para el correo del cliente.
        self.correo_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.correo_cliente.grid(row=1, column=1, padx=10)

# Muestra la etiqueta del campo de teléfono.
        ttk.Label(
            formulario,
            text="Telefono:"
        ).grid(row=2, column=0, padx=10, pady=10)

# Crea el campo de entrada para el teléfono del cliente.
        self.telefono_cliente = ttk.Entry(
            formulario,
            width=30
        )
        self.telefono_cliente.grid(row=2, column=1, padx=10)

# Crea el botón y conecta su acción con registrar_cliente.
        ttk.Button(
            formulario,
            text="Registrar Cliente",
            command=self.registrar_cliente
        ).grid(row=3, column=0, columnspan=2, pady=15)

# Crea la tabla donde se mostrarán los clientes registrados.
        self.tabla_clientes = ttk.Treeview(
            self.pestana_clientes,
            columns=("ID", "Nombre", "Correo", "Telefono"),
            show="headings"
        )

# Recorre los nombres de las columnas para configurarlas.
        for columna in (
            "ID",
            "Nombre",
            "Correo",
            "Telefono"
        ):
# Define el texto del encabezado de la columna actual.
            self.tabla_clientes.heading(
                columna,
                text=columna
            )

# Establece el ancho visual de la columna actual.
            self.tabla_clientes.column(
                columna,
                width=150
            )

# Muestra la tabla y permite que se expanda en el panel.
        self.tabla_clientes.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

# Define la acción que registra un cliente.
    def registrar_cliente(self):

# Inicia el bloque de control de excepciones del registro.
        try:
# Obtiene el nombre y elimina espacios al inicio y al final.
            nombre = self.nombre_cliente.get().strip()
# Obtiene el correo y elimina espacios sobrantes.
            correo = self.correo_cliente.get().strip()
# Obtiene el teléfono y elimina espacios sobrantes.
            telefono = self.telefono_cliente.get().strip()

# Genera un identificador consecutivo según la cantidad de clientes.
            identificador = len(self.clientes) + 1

# Crea el objeto Cliente con el identificador y los datos ingresados.
            cliente = Cliente(
                identificador,
                nombre,
                correo,
                telefono
            )

# Agrega el objeto Cliente a la lista que conserva los datos en memoria.
            self.clientes.append(cliente)

# Inserta una fila en la tabla con los datos del nuevo cliente.
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

# Registra en sistema.log que el cliente fue creado.
            logging.info(
                f"Cliente registrado: {cliente.nombre}"
            )

# Muestra un mensaje para confirmar que el registro fue exitoso.
            messagebox.showinfo(
                "Registro exitoso",
                "El cliente fue registrado correctamente."
            )

# Limpia el campo del nombre después del registro.
            self.nombre_cliente.delete(0, tk.END)
# Limpia el campo del correo después del registro.
            self.correo_cliente.delete(0, tk.END)
# Limpia el campo del teléfono después del registro.
            self.telefono_cliente.delete(0, tk.END)

# Actualiza el selector de clientes disponible en la pestaña Reservas.
            self.actualizar_clientes_reserva()

# Captura los errores que ocurran durante el registro.
        except Exception as error:

# Guarda en el log la información técnica de la excepción.
            logging.exception(
                "Error al registrar cliente"
            )

# Muestra el error en una ventana emergente.
            messagebox.showerror(
                "Error",
                str(error)
            )

    # ---------------- SERVICIOS ----------------

# Define los elementos visuales de la pestaña Servicios.
    def crear_pestana_servicios(self):

# Agrupa los controles para crear un servicio.
        formulario = ttk.LabelFrame(
            self.pestana_servicios,
            text="Crear Servicio"
        )
        formulario.pack(fill="x", padx=15, pady=15)

# Etiqueta que identifica el selector del tipo de servicio.
        ttk.Label(
            formulario,
            text="Tipo de servicio:"
        ).grid(row=0, column=0, padx=10, pady=10)

# Crea una lista desplegable con los tipos de servicio disponibles.
        self.tipo_servicio = ttk.Combobox(
            formulario,
# Define las opciones que puede elegir el usuario.
            values=[
                "Reserva de sala",
                "Alquiler de equipo",
                "Asesoria especializada"
            ],
# Configura la lista para que solo se puedan seleccionar opciones existentes.
            state="readonly"
        )

# Ubica la lista desplegable dentro del formulario.
        self.tipo_servicio.grid(
            row=0,
            column=1,
            padx=10
        )

# Selecciona inicialmente la primera opción de la lista.
        self.tipo_servicio.current(0)

# Etiqueta que identifica el campo del nombre del servicio.
        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=1, column=0, padx=10, pady=10)

# Crea el campo para escribir el nombre del servicio.
        self.nombre_servicio = ttk.Entry(
            formulario,
            width=30
        )
        self.nombre_servicio.grid(
            row=1,
            column=1,
            padx=10
        )

# Etiqueta que identifica el campo del precio por unidad.
        ttk.Label(
            formulario,
            text="Precio por unidad:"
        ).grid(row=2, column=0, padx=10, pady=10)

# Crea el campo donde se ingresa el precio.
        self.precio_servicio = ttk.Entry(
            formulario,
            width=30
        )
        self.precio_servicio.grid(
            row=2,
            column=1,
            padx=10
        )

# Crea el botón que ejecuta crear_servicio.
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

# Crea la tabla donde se mostrarán los servicios registrados.
        self.tabla_servicios = ttk.Treeview(
            self.pestana_servicios,
            columns=("ID", "Tipo", "Nombre", "Precio"),
            show="headings"
        )

# Recorre las columnas para configurar sus encabezados y anchos.
        for columna in (
            "ID",
            "Tipo",
            "Nombre",
            "Precio"
        ):
# Define el texto del encabezado de la columna actual.
            self.tabla_servicios.heading(
                columna,
                text=columna
            )

# Establece el ancho de la columna actual.
            self.tabla_servicios.column(
                columna,
                width=150
            )

# Muestra la tabla de servicios en el panel.
        self.tabla_servicios.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

# Define la lógica para crear el tipo de servicio seleccionado.
    def crear_servicio(self):

# Inicia el bloque de control de errores de creación del servicio.
        try:
# Obtiene el tipo de servicio elegido.
            tipo = self.tipo_servicio.get()
# Obtiene el nombre del servicio y elimina espacios sobrantes.
            nombre = self.nombre_servicio.get().strip()
# Convierte el precio ingresado a un número decimal.
            precio = float(self.precio_servicio.get())

# Genera un identificador consecutivo para el servicio.
            identificador = len(self.servicios) + 1

# Comprueba si el tipo elegido es Reserva de sala.
            if tipo == "Reserva de sala":

# Crea un objeto de la clase ReservaSala.
                servicio = ReservaSala(
                    identificador,
                    nombre,
                    precio
                )

# Si no es Reserva de sala, comprueba si es Alquiler de equipo.
            elif tipo == "Alquiler de equipo":

# Crea un objeto de la clase AlquilerEquipo.
                servicio = AlquilerEquipo(
                    identificador,
                    nombre,
                    precio
                )

# Si no coincide con los tipos anteriores, crea una asesoría especializada.
            else:

# Crea un objeto de la clase AsesoriaEspecializada.
                servicio = AsesoriaEspecializada(
                    identificador,
                    nombre,
                    precio
                )

# Guarda el servicio creado en la lista de servicios.
            self.servicios.append(servicio)

# Agrega una fila a la tabla con los datos del servicio.
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

# Registra en el archivo de log la creación del servicio.
            logging.info(
                f"Servicio creado: {servicio.nombre}"
            )

# Muestra un mensaje de creación exitosa.
            messagebox.showinfo(
                "Servicio creado",
                "El servicio fue creado correctamente."
            )

# Limpia el campo del nombre del servicio.
            self.nombre_servicio.delete(0, tk.END)
# Limpia el campo del precio.
            self.precio_servicio.delete(0, tk.END)

# Actualiza las opciones de servicios disponibles para las reservas.
            self.actualizar_servicios_reserva()

# Captura errores ocurridos durante la creación del servicio.
        except Exception as error:

# Guarda los detalles técnicos del error en el log.
            logging.exception(
                "Error al crear servicio"
            )

# Muestra el error al usuario.
            messagebox.showerror(
                "Error",
                str(error)
            )

    # ---------------- RESERVAS ----------------

# Define los controles visuales de la pestaña Reservas.
    def crear_pestana_reservas(self):

# Crea un recuadro para agrupar el formulario de reservas.
        formulario = ttk.LabelFrame(
            self.pestana_reservas,
            text="Crear Reserva"
        )
        formulario.pack(fill="x", padx=15, pady=15)

# Etiqueta que identifica el selector de clientes.
        ttk.Label(
            formulario,
            text="Cliente:"
        ).grid(row=0, column=0, padx=10, pady=10)

# Crea una lista desplegable para elegir un cliente registrado.
        self.cliente_reserva = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

# Ubica el selector de clientes en el formulario.
        self.cliente_reserva.grid(
            row=0,
            column=1,
            padx=10
        )

# Etiqueta que identifica el selector de servicios.
        ttk.Label(
            formulario,
            text="Servicio:"
        ).grid(row=1, column=0, padx=10, pady=10)

# Crea una lista desplegable para elegir un servicio.
        self.servicio_reserva = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

# Ubica el selector de servicios en el formulario.
        self.servicio_reserva.grid(
            row=1,
            column=1,
            padx=10
        )

# Etiqueta que identifica el campo de duración.
        ttk.Label(
            formulario,
            text="Duracion:"
        ).grid(row=2, column=0, padx=10, pady=10)

# Crea el campo donde se ingresa la duración de la reserva.
        self.duracion_reserva = ttk.Entry(
            formulario,
            width=35
        )

# Ubica el campo de duración en el formulario.
        self.duracion_reserva.grid(
            row=2,
            column=1,
            padx=10
        )

# Crea el botón que ejecuta crear_reserva.
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

# Crea la tabla donde se mostrarán las reservas y sus datos.
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

# Recorre las columnas de la tabla para configurarlas.
        for columna in (
            "ID",
            "Cliente",
            "Servicio",
            "Duracion",
            "Estado",
            "Costo"
        ):
# Define el encabezado de la columna actual.
            self.tabla_reservas.heading(
                columna,
                text=columna
            )

# Establece el ancho de la columna actual.
            self.tabla_reservas.column(
                columna,
                width=130
            )

# Muestra la tabla de reservas y permite que se expanda.
        self.tabla_reservas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

# Crea un contenedor para agrupar los botones de reserva.
        botones = ttk.Frame(
            self.pestana_reservas
        )

        botones.pack(pady=10)

# Crea el botón que confirma la reserva seleccionada.
        ttk.Button(
            botones,
            text="Confirmar Reserva",
            command=self.confirmar_reserva
        ).pack(side="left", padx=5)

# Crea el botón que cancela la reserva seleccionada.
        ttk.Button(
            botones,
            text="Cancelar Reserva",
            command=self.cancelar_reserva
        ).pack(side="left", padx=5)

# Actualiza los clientes disponibles en el selector de reservas.
    def actualizar_clientes_reserva(self):

# Construye las opciones con identificador y nombre de cada cliente.
        self.cliente_reserva["values"] = [
            f"{cliente.identificador} - {cliente.nombre}"
            for cliente in self.clientes
        ]

# Actualiza los servicios disponibles en el selector de reservas.
    def actualizar_servicios_reserva(self):

# Construye las opciones con identificador y nombre de cada servicio.
        self.servicio_reserva["values"] = [
            f"{servicio.identificador} - {servicio.nombre}"
            for servicio in self.servicios
        ]

# Define el proceso para crear una reserva.
    def crear_reserva(self):

# Inicia el bloque de control de errores de creación de la reserva.
        try:
# Obtiene el cliente elegido en la lista desplegable.
            cliente_seleccionado = (
                self.cliente_reserva.get()
            )

# Obtiene el servicio elegido en la lista desplegable.
            servicio_seleccionado = (
                self.servicio_reserva.get()
            )

# Comprueba que se haya seleccionado un cliente.
            if not cliente_seleccionado:
                raise ValueError(
                    "Debe seleccionar un cliente."
                )

# Comprueba que se haya seleccionado un servicio.
            if not servicio_seleccionado:
                raise ValueError(
                    "Debe seleccionar un servicio."
                )

# Convierte la duración ingresada a un número entero.
            duracion = int(
                self.duracion_reserva.get()
            )

# Extrae el identificador del cliente del texto seleccionado.
            cliente_id = int(
                cliente_seleccionado.split(" - ")[0]
            )

# Extrae el identificador del servicio del texto seleccionado.
            servicio_id = int(
                servicio_seleccionado.split(" - ")[0]
            )

# Busca en la lista el objeto Cliente que coincide con ese identificador.
            cliente = next(
                c for c in self.clientes
                if c.identificador == cliente_id
            )

# Busca en la lista el objeto servicio que coincide con ese identificador.
            servicio = next(
                s for s in self.servicios
                if s.identificador == servicio_id
            )

# Genera un identificador consecutivo para la reserva.
            identificador = len(self.reservas) + 1

# Crea el objeto Reserva y relaciona cliente, servicio y duración.
            reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

# Calcula el costo de la reserva usando el método de la clase Reserva.
            costo = reserva.calcular_costo()

# Guarda la reserva en la lista que mantiene los datos en memoria.
            self.reservas.append(reserva)

# Inserta la reserva en la tabla con su estado y costo.
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

# Registra en el log que se creó la reserva.
            logging.info(
                f"Reserva creada: {identificador}"
            )

# Muestra un mensaje de éxito y el costo calculado.
            messagebox.showinfo(
                "Reserva creada",
                f"Reserva creada correctamente.\n"
                f"Costo: ${costo:,.2f}"
            )

# Limpia el campo de duración para el siguiente registro.
            self.duracion_reserva.delete(
                0,
                tk.END
            )

# Captura los errores ocurridos durante la creación de la reserva.
        except Exception as error:

# Guarda en el log los detalles técnicos del error.
            logging.exception(
                "Error al crear reserva"
            )

# Muestra el mensaje de error al usuario.
            messagebox.showerror(
                "Error",
                str(error)
            )

# Define la acción para confirmar una reserva.
    def confirmar_reserva(self):

# Obtiene la fila o filas seleccionadas en la tabla.
        seleccion = (
            self.tabla_reservas.selection()
        )

# Comprueba si el usuario seleccionó una reserva.
        if not seleccion:
# Si no hay selección, muestra una advertencia.
            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva."
            )
# Finaliza el método para no continuar sin una reserva seleccionada.
            return

# Inicia el bloque de control de errores de confirmación.
        try:
# Convierte el identificador seleccionado a entero.
            identificador = int(seleccion[0])

# Busca el objeto Reserva correspondiente al identificador.
            reserva = next(
                r for r in self.reservas
                if r.identificador == identificador
            )

# Ejecuta el método de la reserva que cambia su estado a confirmado.
            reserva.confirmar()

# Actualiza la fila de la tabla con los datos actuales de la reserva.
            self.actualizar_tabla_reserva(
                reserva
            )

# Registra que la reserva fue confirmada.
            logging.info(
                f"Reserva confirmada: {identificador}"
            )

# Informa al usuario que la confirmación fue correcta.
            messagebox.showinfo(
                "Reserva",
                "Reserva confirmada correctamente."
            )

# Captura errores que ocurran durante la confirmación.
        except Exception as error:

# Guarda los detalles técnicos del error en el log.
            logging.exception(
                "Error al confirmar reserva"
            )

# Muestra el error de confirmación al usuario.
            messagebox.showerror(
                "Error",
                str(error)
            )

# Define la acción para cancelar una reserva.
    def cancelar_reserva(self):

# Obtiene la selección actual de la tabla.
        seleccion = (
            self.tabla_reservas.selection()
        )

# Comprueba si el usuario seleccionó una reserva.
        if not seleccion:
# Si no hay selección, muestra una advertencia.
            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva."
            )
# Finaliza el método si no hay una reserva seleccionada.
            return

# Inicia el bloque de control de errores de cancelación.
        try:
# Obtiene el identificador de la reserva seleccionada.
            identificador = int(seleccion[0])

# Busca el objeto Reserva que coincide con el identificador.
            reserva = next(
                r for r in self.reservas
                if r.identificador == identificador
            )

# Ejecuta el método que cambia el estado de la reserva a cancelada.
            reserva.cancelar()

# Actualiza la fila de la tabla con los datos actuales.
            self.actualizar_tabla_reserva(
                reserva
            )

# Registra en el log que la reserva fue cancelada.
            logging.info(
                f"Reserva cancelada: {identificador}"
            )

# Informa al usuario que la cancelación fue correcta.
            messagebox.showinfo(
                "Reserva",
                "Reserva cancelada correctamente."
            )

# Captura errores ocurridos durante la cancelación.
        except Exception as error:

# Guarda los detalles técnicos del error en el log.
            logging.exception(
                "Error al cancelar reserva"
            )

# Muestra el error de cancelación al usuario.
            messagebox.showerror(
                "Error",
                str(error)
            )

# Define el método que actualiza la información de una reserva en la tabla.
    def actualizar_tabla_reserva(self, reserva):

# Calcula nuevamente el costo de la reserva.
        costo = reserva.calcular_costo()

# Actualiza los valores de la fila correspondiente en la tabla.
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


# Este bloque se ejecuta cuando el archivo se inicia directamente.
if __name__ == "__main__":

# Crea la ventana principal de Tkinter.
    ventana = tk.Tk()

# Crea la aplicación y le entrega la ventana principal.
    aplicacion = InterfazSoftwareFJ(
        ventana
    )

# Inicia el ciclo de eventos de Tkinter y mantiene abierta la ventana.
    ventana.mainloop()
