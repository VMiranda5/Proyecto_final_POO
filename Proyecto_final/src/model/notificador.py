from src.model.notificacion import Notificacion
from src.model.siembra import Siembra

class Notificador:
      def __init__(self) -> None:
            self.notificaciones:list[Notificacion]=[]
            self.mensajes_de_notificacion:dict(Siembra,str)={}
      
      def verificar_notificaciones(self):
           #print('se esta ejecutando la verificacion de notificacione')
           for notificacion in self.notificaciones:
               #print(notificacion.dias_para_germinacion)
               if notificacion.dias_para_germinacion!=None and notificacion.dias_para_germinacion>=notificacion.siembra.semilla.tiempo_germinacion:
                  #print("se va a agregar la notificacion")
                  self.mensajes_de_notificacion[notificacion.siembra]="Listo para germinar"

               elif notificacion.dias_para_cosecha!=None and notificacion.dias_para_cosecha>=notificacion.siembra.semilla.tiempo_cosecha:
                       self.mensajes_de_notificacion[notificacion.siembra]="listo para cosecha"

               elif notificacion.dias_para_germinacion==None and notificacion.dias_para_cosecha==None:
                       self.notificaciones.remove(notificacion)

      
      def cambiar_estado(self, id_siembra:str, estado:str):
            for notificacion in self.notificaciones:
                  if notificacion.siembra.id_siembra==id_siembra:
                        notificacion.siembra.estado=estado
                        self.reiniciar_notificacion(notificacion)
                        #self.notificaciones.remove(notificacion)
                        #self.notificaciones.append(Notificacion(notificacion.siembra))
                        #del self.mensajes_de_notificacion[notificacion.siembra]
                        #self.verificar_notificaciones()

      def reiniciar_notificacion(self, notificacion:Notificacion):
            self.notificaciones.remove(notificacion)
            self.notificaciones.append(Notificacion(notificacion.siembra))
            del self.mensajes_de_notificacion[notificacion.siembra]
            self.verificar_notificaciones()
