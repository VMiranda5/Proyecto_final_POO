import pickle
from src.model.semilla import Semilla
from src.model.siembra import Siembra
from src.model.notificacion import Notificacion
from src.model.notificador import Notificador
from src.model.semilla_no_registrada_error import SemillaNoRegistradaError
from src.model.semilla_existente_error import SemillaExistenteError
#ESTADOS = ('germinando','sembrado','cosechado')
#DATE_FORMAT = "%d-%m-%Y"


class Huerta:
      def __init__(self):
            self.inventario:list[Semilla]=[]
            self.registros:dict(str,Semilla)={}
            self.notificador:Notificador=Notificador()
            self.cargar_inventario()
            self.cargar_registros()
            self.cargar_notificaciones()
        
      def agregar_semilla(self,especie:str, tiempo_germinacion:int, tiempo_cosecha:int, lugar:str):
            #print(self.semilla_en_inventario(especie))
            if self.semilla_en_inventario(especie) != None:
                  raise SemillaExistenteError(especie)
            else:
                  self.inventario.append(Semilla(especie,tiempo_germinacion,tiempo_cosecha,lugar))
                  self.guardar_inventario()

      def cargar_inventario(self):
            try:
                  with open("inventario.pickle", "rb") as archivo:
                        self.inventario = pickle.load(archivo)
                        #print("Inventario cargado con éxito")
            except EOFError:
            # Handle the case when the file is empty
                  self.inventario = []  # Initialize self.inventario as an empty list
                  #print("Inventario está vacío")
            except Exception as e:
                  print(f"An error occurred: {e}")

      def guardar_inventario(self):
            with open("inventario.pickle","wb") as archivo:
                  pickle.dump(self.inventario, archivo)

      def cargar_notificaciones(self):
            try:
                  with open("notificaciones.pickle","rb") as archivo:
                        self.notificador.notificaciones=pickle.load(archivo)
                        #print("notificaciones cargadas con exito")
            except EOFError:
                  self.notificador.notificaciones=[]
            except Exception as e:
                  print(f"an error occurred: {e}")

      def guardar_notificaciones(self):
            with open("notificaciones.pickle", "wb") as archivo:
                  pickle.dump(self.notificador.notificaciones, archivo)


      def cargar_registros(self):
            try:
                  with open("registros.pickle", "rb") as archivo:
                        self.registros = pickle.load(archivo)
                        #print("Registros cargados con éxito")
            except EOFError:
            # Handle the case when the file is empty
                  self.registros = {}  # Initialize self.registros as an empty list
                  #print("Registros están vacíos")
            except Exception as e:
                  self.registros = []  # Initialize self.registros as an empty list
                  print(f"An error occurred: {e}")

      def guardar_registros(self):
            with open("registros.pickle","wb") as archivo:
                  pickle.dump(self.registros, archivo)

      def semilla_en_inventario(self,especie:str):
            var=None
            for i in self.inventario:
                  if i.especie==especie:
                        var=i
                        break     
            return var

      #def revisar_lugar(self, siembra:Siembra)->bool:
            #return siembra.lugar==siembra.semilla.lugar
        
      def agregar_siembra(self, especie:str, cantidad:int, fecha:str, lugar:str):
            if self.semilla_en_inventario(especie)==None:
                  raise SemillaNoRegistradaError(especie)
            else:
                  nueva_siembra=Siembra(self.semilla_en_inventario(especie),cantidad,fecha,lugar)
                  self.registros[nueva_siembra.id_siembra]=nueva_siembra
                  #self.notificador.notificaciones.append(Notificacion(nueva_siembra))
                  self.inicializar_notificacion(nueva_siembra)
                  self.guardar_registros()
                  self.guardar_notificaciones()
                  return(nueva_siembra.id_siembra)
            
      def inicializar_notificacion(self,nueva_siembra:Siembra):
            self.notificador.notificaciones.append(Notificacion(nueva_siembra))

      def guardar_kg_cosechados(self, id_siembra:str, kg_cosechados):
            self.registros[id_siembra].kg_cosechados= kg_cosechados
