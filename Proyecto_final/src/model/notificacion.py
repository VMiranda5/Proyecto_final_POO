from src.model.siembra import Siembra
from datetime import datetime

class Notificacion:
     def __init__(self, siembra:Siembra) -> None:
          self.siembra=siembra
          self.fecha_actual = datetime.now()
          #self.dias_para_germinacion = 0
          #self.dias_para_cosecha= 0
          #print(self.siembra.estado=='germinando')
          if self.siembra.estado=='germinando':                  
               self.dias_para_germinacion= (self.fecha_actual-self.siembra.fecha_siembra).days
               self.dias_para_cosecha=None
               #print(self.dias_para_germinacion)
          elif self.siembra.estado=='sembrado':
               self.dias_para_cosecha=(self.fecha_actual-self.siembra.fecha_siembra).days
               self.dias_para_germinacion=None
          else:
               self.dias_para_germinacion = None
               self.dias_para_cosecha=None

