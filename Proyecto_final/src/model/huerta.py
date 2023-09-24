from dataclasses import dataclass
from datetime import datetime
ESTADOS = ('germinando','sembrado','cosechado')
DATE_FORMAT = "%d-%m-%Y"


@dataclass
class Semilla:
    especie:str
    tiempo_germinacion:int
    tiempo_cosecha:int
    lugar:str

        
class Siembra:
      cont=0
      def __init__(self, especie:Semilla, cantidad:int,fecha:str, lugar:str):
            self.semilla:Semilla=especie
            self.cantidad_semillas: int=cantidad
            self.fecha_siembra:datetime =datetime.strptime(fecha, DATE_FORMAT)
            self.lugar: str=lugar
            self.estado: str = ESTADOS[0]
            self.kg_cosechados: float= 0.0
            self.id_siembra:int=Siembra.cont
            Siembra.cont+=1
      def __repr__(self):
        return f'Siembra({self.semilla}, {self.cantidad_semillas}, {self.fecha_siembra}, {self.lugar}, {self.estado})'


class Notificacion:
     def __init__(self, siembra:Siembra) -> None:
          self.dias_restantes:int

class Notificador:
      def __init__(self) -> None:
            self.notificaciones:list[Notificacion]=[]
      
      def mostrar_notificacion(self):
           pass
      
      def cambiar_estado(self):
           pass

class Huerta:
      def __init__(self):
            self.inventario:list[Semilla]=[]
            self.registros:dict(str,Semilla)={}
            self.notificador:Notificador
        
      def agregar_semilla(self,especie:str, tiempo_germinacion:int, tiempo_cosecha:int, lugar:str):
            self.inventario.append(Semilla(especie,tiempo_germinacion,tiempo_cosecha,lugar))

      def semilla_en_inventario(self,especie:str):
        for i in self.inventario:
            if i.especie==especie:
                  return i
            else:
                  return None

      def revisar_lugar(self, siembra:Siembra)->bool:
            return siembra.lugar==siembra.semilla.lugar
        
      def agregar_siembra(self, especie:str, cantidad:int, fecha:str, lugar:str):
            nueva_siembra=Siembra(self.semilla_en_inventario(especie),cantidad,fecha,lugar)
            self.registros[nueva_siembra.id_siembra]=nueva_siembra
        
      def cambio_lugar(self,id_siembra:str, lugar:str):
            self.registros[id_siembra].lugar = lugar
        
      def reiniciar_notificador(self):
            pass

      def desactivar_notificador(self):
            pass

      def guardar_kg_cosechados(self, id_siembra:str, kg_cosechados):
            self.registros[id_siembra].kg_cosechados= kg_cosechados
