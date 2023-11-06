import tkinter as tk

class FrameNotificacion(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title=("Notificaciones")

        label = tk.Label(self, text="Tiene notificaciones pendientes\n por favor ingrese a la opción de revisar notificaciones")
        label.grid(column=0,row=0)
        boton_ok= tk.Button(self, text="OK", command=self.destroy)
        boton_ok.grid(column=0,row=1)