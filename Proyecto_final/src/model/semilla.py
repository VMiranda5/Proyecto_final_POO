from dataclasses import dataclass

@dataclass
class Semilla:
    especie:str
    tiempo_germinacion:int
    tiempo_cosecha:int
    lugar:str

    def __str__(self) -> str:
        return f'Especie: {self.especie}\ntiempo de germinación: {self.tiempo_germinacion}\n tiempo de cosecha: {self.tiempo_cosecha}\n lugar óptimo: {self.lugar}\n'