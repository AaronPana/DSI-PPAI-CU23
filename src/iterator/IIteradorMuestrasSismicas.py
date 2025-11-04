from .IIterador import IIterador
from typing import List
from entities.MuestraSismica import MuestraSismica

# - listaMuestrasSismicas: list[MuestraSismica]
# - posicionActual: int
# + new(listaElementos: list[object]): IIterador
# + primero(): None
# + haFinalizado(): bool
# + elementoActual(): object
# + siguiente(): None

class IteradorMuestrasSismicas(IIterador):
    def __init__(self, listaElementos: List[MuestraSismica]):
        self.listaMuestrasSismicas: List[MuestraSismica] = listaElementos
        self.posicionActual: int = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaMuestrasSismicas)

    def elementoActual(self) -> object:
        if not self.haFinalizado():
            return self.listaMuestrasSismicas[self.posicionActual]
        return None
    
    def comprobarFiltro(self):
        pass

    def siguiente(self) -> None:
        self.posicionActual += 1