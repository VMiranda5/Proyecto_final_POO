import tkinter as tk
from src.GUI.frame_agregar_semilla import FrameAgregarSemilla
from src.GUI.main_frame import MainFrame
from src.GUI.frame_agregar_nueva_siembra import FrameAgregarNuevaSiembra
from src.GUI.frame_ver_inventario import FrameVerInventario
from src.GUI.frame_ver_registros import FrameVerRegistros
from src.GUI.frame_notificacion import FrameNotificacion
from src.GUI.frame_ver_notificaciones import FrameVerNotificaciones
from src.GUI.frame_cambiar_estado import FrameCambiarEstado
from src.GUI.frame_registrar_kg import FrameRegistrarKg
from src.model.huerta import Huerta

class MainApplication:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Sistema de registro y seguimiento Ecohuerta UdeM")
        self.huerta = Huerta() #inicializar el objeto huerta
        

        #inicializa todos los frames
        self.main_frame = MainFrame(self.root, self.huerta)
        self.frame_agregar_semilla= FrameAgregarSemilla(self.root, self.huerta)
        self.frame_agregar_nueva_siembra = FrameAgregarNuevaSiembra(self.root,self.huerta)
        self.frame_ver_inventario = FrameVerInventario(self.root, self.huerta)
        self.frame_ver_registros = FrameVerRegistros(self.root,self.huerta)
        self.frame_ver_notificaciones = FrameVerNotificaciones(self.root, self.huerta)
        self.frame_cambiar_estado = FrameCambiarEstado(self.root, self.huerta)
        self.frame_registrar_kg=FrameRegistrarKg(self.root, self.huerta)

        #botones de navegacion
        self.boton_inicio = tk.Button(self.root, text= "Inicio", command = self.cambiar_a_main)

        self.boton_agregar_semilla = tk.Button(self.root, text="Agregar semilla al inventario", command=self.cambiar_a_agregar_semilla)

        self.boton_agregar_nueva_siembra = tk.Button(self.root, text="Registrar una siembra nueva", command=self.cambiar_a_agregar_nueva_siembra)

        self.boton_ver_inventario = tk.Button(self.root, text="Ver inventario de semillas registradas", command=self.cambiar_a_ver_inventario)

        self.boton_ver_registros= tk.Button(self.root, text="ver registro de siembras realizadas",command=self.cambiar_a_ver_registros)

        self.boton_ver_notificaciones=tk.Button(self.root, text="ver las notificaciones pendientes", command=self.cambiar_a_ver_notificaciones)

        self.boton_cambiar_estado= tk.Button(self.root, text="cambiar estado de una siembra", command=self.cambiar_a_cambiar_estado)

        self.boton_registrar_kg= tk.Button(self.root, text="registrar kg de una siembra", command=self.cambiar_a_registrar_kg)

        self.boton_salir=tk.Button(self.root, text="salir", command=self.salir)

        #grid layout for buttons
        self.boton_inicio.grid(row=2,column=0)
        self.boton_agregar_semilla.grid(row=3,column=0)
        self.boton_agregar_nueva_siembra.grid(row=4, column=0)
        self.boton_ver_inventario.grid(row=5, column=0)
        self.boton_ver_registros.grid(row=6,column=0)
        self.boton_ver_notificaciones.grid(row=7, column=0)
        self.boton_cambiar_estado.grid(row=8,column=0)
        self.boton_registrar_kg.grid(row=9,column=0)
        self.boton_salir.grid(row=10,column=0)
    
        #que inicialmente muestre el frame principal
        self.cambiar_a_main()

    #funcion que muestra en main frame y cierra los otros
    def cambiar_a_main(self):
        self.main_frame.grid(row=1,column=0)
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.huerta.notificador.verificar_notificaciones()
        #print(self.huerta.notificador.notificaciones)
        #print(self.huerta.notificador.mensajes_de_notificacion)
        if len(self.huerta.notificador.mensajes_de_notificacion)!=0:
            self.frame_notificacion= FrameNotificacion(self.root)
            self.frame_notificacion

    def cambiar_a_agregar_semilla(self):
        self.main_frame.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_agregar_semilla.grid(row=1, column=1)

    def cambiar_a_agregar_nueva_siembra(self):
        self.main_frame.grid_forget()
        self.frame_agregar_semilla.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_agregar_nueva_siembra.grid(row=1, column=1)

    def cambiar_a_ver_inventario(self):
        self.main_frame.grid_forget()
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_ver_inventario.grid(row=1,column=1)

    def cambiar_a_ver_registros(self):
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.main_frame.grid_forget()
        self.frame_ver_inventario.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_ver_registros.grid(row=1,column=1)

    def cambiar_a_ver_notificaciones(self):
        self.main_frame.grid_forget()
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_ver_notificaciones = FrameVerNotificaciones(self.root, self.huerta)
        self.frame_ver_notificaciones.grid(row=1,column=1)

    def cambiar_a_cambiar_estado(self):
        self.main_frame.grid_forget()
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        self.frame_registrar_kg.destroy()
        self.frame_cambiar_estado = FrameCambiarEstado(self.root, self.huerta)
        self.frame_cambiar_estado.cargar_siembras()
        self.frame_cambiar_estado.grid(row=1,column=1)

    def cambiar_a_registrar_kg(self):
        self.main_frame.grid_forget()
        self.frame_agregar_semilla.grid_forget()
        self.frame_agregar_nueva_siembra.grid_forget()
        self.frame_ver_inventario.grid_forget()
        self.frame_ver_registros.grid_forget()
        #self.frame_ver_notificaciones.grid_forget()
        self.frame_ver_notificaciones.destroy()
        #self.frame_cambiar_estado.grid_forget()
        self.frame_cambiar_estado.destroy()
        self.frame_registrar_kg=FrameRegistrarKg(self.root, self.huerta)
        self.frame_registrar_kg.cargar_siembras_cosechadas()
        self.frame_registrar_kg.grid(row=1,column=1)

    def salir(self):
        self.root.quit()

