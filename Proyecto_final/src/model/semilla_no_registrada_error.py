from src.model.semilla import Semilla
from src.model.semilla_error import SemillaError

class SemillaNoRegistradaError(SemillaError):
    def __init__(self, especie:str):
        super().__init__()
        self.especie = especie

    def __str__(self) -> str:
        return f"la semilla de {self.especie} no está registrada en el inventario, por favor regístrela antes de crear la nueva siembra"