import tkinter as tk
from src.model.huerta import Huerta
from src.model.semilla_existente_error import SemillaExistenteError

class FrameAgregarSemilla(tk.Frame):
    def __init__(self, master, huerta:Huerta):
        super().__init__(master)
        label= tk.Label(self, text="agregar semilla al inventario",font="system")
        label.grid(row=0, column=1)

        self.huerta:Huerta = huerta

        #recibe el nombre de la especie
        tk.Label(self, text="Nombre de la especie").grid(column=1,row=1)
        self.especie=tk.StringVar()
        entry_especie = tk.Entry(self,textvariable=self.especie)
        entry_especie.grid(column=2, row=1)

        #recibe el tiempo de germinacion (en dias)
        tk.Label(self, text="tiempo de germinación (en días)").grid(column=1,row=2)
        self.tiempo_germinacion = tk.IntVar()
        entry_tiempo_germinacion = tk.Entry(self, textvariable=self.tiempo_germinacion)
        entry_tiempo_germinacion.grid(column=2,row=2)

        #recibe el tiempo de cosecha
        tk.Label(self, text="tiempo de cosecha (en días)").grid(column=1, row=3)
        self.tiempo_cosecha = tk.IntVar()
        entry_tiempo_cosecha= tk.Entry(self, textvariable=self.tiempo_cosecha)
        entry_tiempo_cosecha.grid(column=2, row=3)

        #recibe el lugar optimo para crecimiento
        tk.Label(self, text="¿Cuál es el lugar óptimo para su crecimiento?").grid(column=1,row=4)
        self.lugar_optimo = tk.StringVar()
        entry_lugar_optimo = tk.Entry(self, textvariable=self.lugar_optimo)
        entry_lugar_optimo.grid(column=2, row=4)

        #despues de ingresar todos los valores, se agrega la semilla
        tk.Button(self, text="guardar información registrada", command=self.registrar_semilla).grid(column=2, row=5)
        
    def registrar_semilla(self):
        try:
            self.huerta.agregar_semilla(self.especie.get(),self.tiempo_germinacion.get(), self.tiempo_cosecha.get(), self.lugar_optimo.get())
            #print("done")
            #print(self.huerta.inventario)
        except SemillaExistenteError:
            error=tk.Toplevel(self)
            error.title("error: semilla existente")
            label=tk.Label(error,text=f"error: la semilla ya está registrada en el inventario")
            label.grid(column=0,row=0)
            boton_error=tk.Button(error,text="OK", command=error.destroy)
            boton_error.grid(column=0,row=1)