import tkinter as tk
from src.model.huerta import Huerta

class FrameCambiarEstado(tk.Frame):
    def __init__(self,master,huerta:Huerta):
        super().__init__(master)
        label = tk.Label(self, text="Cambie el estado de una siembra después de haber recibido la notificación")
        label.grid(row=0,column=1)

        self.huerta:Huerta = huerta

        self.estado_seleccionado=tk.StringVar()
        self.listbox= tk.Listbox(self)
        self.listbox.grid(row=1,column=2)

        self.siembra_seleccionada=tk.StringVar()
        self.listbox_siembra_id=tk.Listbox(self)
        self.listbox_siembra_id.grid(row=1,column=1)

        
        self.estados =('germinando','sembrado','cosechado')

        for estado in self.estados:
            #print("los estados iteran")
            self.listbox.insert(tk.END,estado)

        boton_seleccionar_estado=tk.Button(self,text="seleccionar estado",command=self.seleccionar_estado)
        boton_seleccionar_estado.grid(column=2,row=6)

        boton_seleccionar_siembra=tk.Button(self,text="seleccionar siembra", command=self.seleccionar_siembra)
        boton_seleccionar_siembra.grid(column=1,row=6)

        boton_cambiar_estado = tk.Button(self,text="cambiar estado",command=self.cambiar_estado)
        boton_cambiar_estado.grid(column=2,row=7)

    def cambiar_estado(self):
        self.huerta.notificador.cambiar_estado(self.siembra_seleccionada,self.estado_seleccionado)
        self.huerta.registros[self.siembra_seleccionada].estado=self.estado_seleccionado
        self.huerta.guardar_registros()
        self.huerta.guardar_notificaciones()
        #print(self.huerta.notificador.notificaciones)

    def cargar_siembras(self):
        for identificador in self.huerta.notificador.mensajes_de_notificacion.keys():
            print("la lista de notificaciones esta cargando")
            self.listbox_siembra_id.insert(tk.END,identificador.id_siembra)


    def seleccionar_estado(self):
        selected_index=self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index[0])
            self.estado_seleccionado.set(selected_item)
            self.estado_seleccionado=self.estado_seleccionado.get()
        else:
            self.estado_seleccionado.set("no se ha seleccionado un estado")
        #print(self.estado_seleccionado)

    def seleccionar_siembra(self):
        selected_index=self.listbox_siembra_id.curselection()
        if selected_index:
            selected_item = self.listbox_siembra_id.get(selected_index[0])
            self.siembra_seleccionada.set(selected_item)
            self.siembra_seleccionada=self.siembra_seleccionada.get()
        else:
            self.siembra_seleccionada.set("no se ha seleccionado una siembra")
        #print(self.siembra_seleccionada)

       