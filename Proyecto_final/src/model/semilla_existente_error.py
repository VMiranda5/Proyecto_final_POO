from src.model.semilla_error import SemillaError

class SemillaExistenteError(SemillaError):
    def __init__(self, especie:str):
        super().__init__()
        self.especie = especie

    def __str__(self) -> str:
        return f"la semilla que intenta agregar al inventario ya se encuentra registrada"