import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from src.model.huerta import Huerta
from src.model.semilla_no_registrada_error import SemillaNoRegistradaError


class FrameAgregarNuevaSiembra(tk.Frame):
    def __init__(self, master, huerta:Huerta):
        super().__init__(master)
        label= tk.Label(self, text="agregar una siembra nueva",font="system")
        label.grid(row=0, column=1)

        self.huerta:Huerta = huerta

        #recibe el nombre de la especie de semillas que se sembraron
        tk.Label(self, text="Nombre de la especie sembrada").grid(column=1,row=1)
        self.especie=tk.StringVar()
        entry_especie = tk.Entry(self,textvariable=self.especie)
        entry_especie.grid(column=2, row=1)

        #recibe la cantidad de semillas sembradas
        tk.Label(self, text="cantidad de semillas sembradas").grid(column=1,row=2)
        self.cantidad_semillas = tk.IntVar()
        entry_cantidad_semillas = tk.Entry(self, textvariable=self.cantidad_semillas)
        entry_cantidad_semillas.grid(column=2,row=2)

        #recibe lugar donde se hizo la siembra
        tk.Label(self, text="lugar donde se realizó la siembra").grid(column=1,row=3)
        self.lugar_siembra = tk.StringVar()
        entry_lugar_siembra = tk.Entry(self, textvariable=self.lugar_siembra)
        entry_lugar_siembra.grid(column=2,row=3)

        #recibe la fecha de siembra
        tk.Label(self, text="fecha de la siembra").grid(column=1,row=4)
        self.cal:Calendar = Calendar(self, selectmode="day", date_pattern="dd-mm-yyyy")
        self.cal.grid(column=2, row=4)

        tk.Button(self, text="seleccionar fecha",command=self.guardar_fecha).grid(column=2,row=5)
        self.date_label = tk.Label(self, text="")
        self.date_label.grid(column=2, row=6)

        #se guardan los datos
        tk.Button(self, text="registrar siembra", command=self.agregar_siembra). grid(column=1, row=7)



    def guardar_fecha(self):
        self.fecha = self.cal.get_date()
        self.date_label.config(text=f"Fecha seleccionada: {self.fecha}")

    def agregar_siembra(self):
        try:
            id_siembra=self.huerta.agregar_siembra(self.especie.get(), self.cantidad_semillas.get(),self.fecha, self.lugar_siembra.get())
            mostrar_id=tk.Toplevel(self)
            #mostrar_id.grid(column=1,row=1)
            mostrar_id.title("ID de la siembra")
            label=tk.Label(mostrar_id,text=f"el ID asignado a la siembra es:\n {id_siembra}")
            label.grid(column=0,row=0)
            boton_ok=tk.Button(mostrar_id,text="OK", command=mostrar_id.destroy)
            boton_ok.grid(column=0,row=1)
            #print(self.huerta.registros)
        except SemillaNoRegistradaError:
            error=tk.Toplevel(self)
            #mostrar_id.grid(column=1,row=1)
            error.title("error: semilla no registrada")
            label=tk.Label(error,text=f"error: semilla no registrada\n regístrela antes de agregar la siembra")
            label.grid(column=0,row=0)
            boton_error=tk.Button(error,text="OK", command=error.destroy)
            boton_error.grid(column=0,row=1)