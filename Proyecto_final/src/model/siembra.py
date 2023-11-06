from src.model.semilla import Semilla
from datetime import datetime
import uuid
import time
ESTADOS = ('germinando','sembrado','cosechado')
DATE_FORMAT = "%d-%m-%Y"

class Siembra:
      def __init__(self, especie:Semilla, cantidad:int,fecha:str, lugar:str):
            self.semilla:Semilla=especie
            self.cantidad_semillas: int=cantidad
            self.fecha_siembra:datetime =datetime.strptime(fecha, DATE_FORMAT)
            self.lugar: str=lugar
            self.estado: str = ESTADOS[0]
            self.kg_cosechados: float= 0.0
            self.id_siembra:str=self.get_ID()


      def __repr__(self):
            if self.estado=="cosechado": 
                  return f'Especie: {self.semilla.especie}\nCantidad de semillas: {self.cantidad_semillas}\nfecha de la siembra: {self.fecha_siembra}\nlugar de la siembra: {self.lugar}\n estado de la siembra: {self.estado}\nkg cosechados: {self.kg_cosechados}\nID:{self.id_siembra}'
        
            else:
                  return f'Especie: {self.semilla.especie}\nCantidad de semillas: {self.cantidad_semillas}\nfecha de la siembra: {self.fecha_siembra}\nlugar de la siembra: {self.lugar}\n estado de la siembra: {self.estado}\nID:{self.id_siembra}'
        
             
      def get_ID(self):
           unique_id=str(uuid.uuid4())[:8]
           id=f"{int(time.time())}_{unique_id}"
           return id