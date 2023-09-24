import sys
import datetime
from src.model.huerta import Huerta
from src.model.huerta import Semilla


class UIConsola:

    def __init__(self):
        self.huerta: Huerta = Huerta()
        self.opciones = {
            "1": self.registrar_semilla,
            "2": self.registrar_siembra,
            "3": self.cambiar_lugar,
            "4": self.ver_inventario,
            "5": self.ver_siembras,
            "6": self.salir
        }

    @staticmethod
    def mostrar_menu():
        titulo = "Ecohuerta UdeM"
        print(f"\n{titulo:_^30}")
        print("1. Registrar semilla")
        print("2. Registrar siembra")
        print("3. Cambiar lugar de siembra")
        print("4. Ver lista de semillas registradas")
        print("5. Ver registro de siembras realizadas")
        print("6. salir")
        print(f"{'_':_^30}")


    def ejecutar_app(self):
        print("Bienvenido al sistema de registro y seguimiento de la Ecohuerta UdeM\n")
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def registrar_semilla(self):
        especie:str=input('¿Cuál es el nombre de la especie a registrar? -> ')
        tiempo_germinacion:int=int(input('¿Cuántos días se tarda en germinar? -> '))
        tiempo_cosecha:int=int(input('¿Cuántos días se tarda en dar cosecha? -> '))
        lugar:str=input('¿Cuál es el lugar óptimo para su desarrollo? -> ')
        self.huerta.agregar_semilla(especie, tiempo_germinacion,tiempo_cosecha,lugar)

    
    def registrar_siembra(self):
        especie:str=input('¿Cuál especie se sembró? -> ')
        cantidad:int=int(input('¿Cuántas semillar se sembraron? -> '))
        fecha:str=input('¿En qué día se sembró (indique en formato dd-mm-aaaa? -> ')
        lugar:str=input('¿En dónde se sembró? -> ')
        self.huerta.agregar_siembra(especie, cantidad, fecha, lugar)
        
            

    def cambiar_lugar(self):
        pass

    def ver_inventario(self):
        print(self.huerta.inventario)

    def ver_siembras(self):
        print(self.huerta.registros)

    @staticmethod
    def salir():
        print("\nGRACIAS POR USAR EL PROGRAMA. VUELVA PRONTO")
        sys.exit(0)
