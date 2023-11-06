import tkinter as tk
from src.model.huerta import Huerta

class FrameVerNotificaciones(tk.Frame):
    def __init__(self, master, huerta: Huerta):
        super().__init__(master)
        label = tk.Label(self, text="Tiene las siguientes notificaciones:", font="system")
        label.grid(row=0, column=1)

        self.huerta: Huerta = huerta
        tk.Button(self, text="actualizar lista", command=self.mostrar_notificaciones).grid(column=1, row=1)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=2, column=1)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=2, column=2, sticky="ns")
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

    def mostrar_notificaciones(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        n = 0
        for notificacion in self.huerta.notificador.mensajes_de_notificacion:
            label = tk.Label(self.frame, text=f"INFORMACIÓN DE LA SIEMBRA:\n{notificacion}\n MENSAJE: \n{self.huerta.notificador.mensajes_de_notificacion[notificacion]}")
            label.grid(row=n, column=0, sticky="w")
            n += 1

        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
