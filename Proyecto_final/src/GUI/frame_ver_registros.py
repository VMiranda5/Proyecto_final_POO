import tkinter as tk
from src.model.huerta import Huerta

class FrameVerRegistros(tk.Frame):
    def __init__(self, master, huerta: Huerta):
        super().__init__(master)

        label = tk.Label(self, text="Estos son los registros de siembras realizadas", font="system")
        label.grid(row=0, column=1)

        self.huerta: Huerta = huerta

        tk.Button(self, text="actualizar lista", command=self.mostrar_siembras).grid(column=1, row=1)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=2, column=1)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=2, column=2, sticky="ns")
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

    def mostrar_siembras(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        n = 0
        for siembra in self.huerta.registros:
            label = tk.Label(self.frame, text=f"ID: {siembra}\n {self.huerta.registros[siembra]}")
            label.grid(row=n, column=0, sticky="w")
            n += 1

        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
