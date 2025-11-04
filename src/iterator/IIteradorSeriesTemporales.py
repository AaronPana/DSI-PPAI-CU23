from .IIterador import IIterador
from typing import List
from entities.SerieTemporal import SerieTemporal

# - listaSeriesTemporales: list[SerieTemporal]
# - posicionActual: int
# + new(listaElementos: list[object]): IIterador
# + primero(): None
# + haFinalizado(): bool
# + elementoActual(): object
# + siguiente(): None

class IteradorSeriesTemporales(IIterador):
    def __init__(self, listaElementos: List[SerieTemporal]):
        self.listaSeriesTemporales: List[SerieTemporal] = listaElementos
        self.posicionActual = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaSeriesTemporales)

    def elementoActual(self) -> object:
        if not self.haFinalizado():
            return self.listaSeriesTemporales[self.posicionActual]
        return None
    
    def comprobarFiltro(self):
        pass

    def siguiente(self) -> None:
        self.posicionActual += 1