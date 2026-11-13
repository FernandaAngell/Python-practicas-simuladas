            self.actualizar_tabla_reserva(
                reserva
            )

            # Registra la operación.
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

        # Obtiene la reserva seleccionada.
        seleccion = (
            self.tabla_reservas.selection()
        )

        # Verifica que exista una selección.
        if not seleccion:
            messagebox.showwarning(
                "Atencion",
                "Seleccione una reserva."
            )
            return

        try:
            # Obtiene el identificador de la reserva.
            identificador = int(seleccion[0])

            # Busca la reserva dentro de la lista.
            reserva = next(
                r for r in self.reservas
                if r.identificador == identificador
            )

            # Cambia el estado de la reserva a cancelada.
            reserva.cancelar()

            # Actualiza la información de la tabla.
            self.actualizar_tabla_reserva(
                reserva
            )

            # Registra la cancelación.
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

        # Recalcula el costo de la reserva.
        costo = reserva.calcular_costo()

        # Actualiza la fila correspondiente en el Treeview.
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


# Punto de entrada principal del programa.
# Solo se ejecuta cuando este archivo se ejecuta directamente.
if __name__ == "__main__":

    # Crea la ventana principal de Tkinter.
    ventana = tk.Tk()

    # Crea la aplicación y le entrega la ventana principal.
    aplicacion = InterfazSoftwareFJ(
        ventana
    )

    # Mantiene abierta la interfaz gráfica.
    ventana.mainloop()

