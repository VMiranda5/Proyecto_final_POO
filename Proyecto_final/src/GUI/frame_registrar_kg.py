import tkinter as tk
from src.model.huerta import Huerta

class FrameRegistrarKg(tk.Frame):
    def __init__(self,master,huerta:Huerta):
        super().__init__(master)
        label= tk.Label(self,text="Registrar kg cosechados de una siembra")
        label.grid(row=0,column=1)

        self.huerta:Huerta= huerta

        tk.Label(self, text="seleccione la siembra").grid(column=1, row=1)
        self.siembra_seleccionada=tk.StringVar()
        self.listbox_siembra_id=tk.Listbox(self)
        self.listbox_siembra_id.grid(row=2,column=1)

        boton_seleccionar_siembra=tk.Button(self,text="seleccionar siembra", command=self.seleccionar_siembra)
        boton_seleccionar_siembra.grid(column=1,row=6)

        tk.Label(self,text="kg cosechados ").grid(column=1,row=7)
        self.kg_cosechados = tk.DoubleVar()
        entry_kg_cosechados=tk.Entry(self,textvariable=self.kg_cosechados)
        entry_kg_cosechados.grid(column=2,row=7)

        tk.Button(self, text="registrar kg cosechados", command=self.registrar_kg). grid(column=1, row=8)

    def cargar_siembras_cosechadas(self):
        for siembra in self.huerta.registros:
            if self.huerta.registros[siembra].estado=="cosechado":
                self.listbox_siembra_id.insert(tk.END, siembra)

    def registrar_kg(self):
        self.kg_cosechados=self.kg_cosechados.get()
        #self.huerta.registros[self.siembra_seleccionada].kg_cosechados = self.kg_cosechados
        self.huerta.guardar_kg_cosechados(self.siembra_seleccionada,self.kg_cosechados)
        self.huerta.guardar_registros()

    def seleccionar_siembra(self):
        selected_index=self.listbox_siembra_id.curselection()
        if selected_index:
            selected_item = self.listbox_siembra_id.get(selected_index[0])
            self.siembra_seleccionada.set(selected_item)
            self.siembra_seleccionada=self.siembra_seleccionada.get()
        else:
            self.siembra_seleccionada.set("no se ha seleccionado una siembra")
        #print(self.siembra_seleccionada)
