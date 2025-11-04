from .IIterador import IIterador
from typing import List
from entities.DetalleMuestraSismica import DetalleMuestraSismica

# - listaDetallesMuestraSismica: list[DetalleMuestraSismica]
# - posicionActual: int
# + new(listaElementos: list[object]): IIterador
# + primero(): None
# + haFinalizado(): bool
# + elementoActual(): object
# + siguiente(): None

class IteradorDetallesMuestraSismica(IIterador):
    def __init__(self, listaElementos: List[DetalleMuestraSismica]):
        self.listaDetallesMuestraSismica: List[DetalleMuestraSismica] = listaElementos
        self.posicionActual: int = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaDetallesMuestraSismica)

    def elementoActual(self) -> object:
        if not self.haFinalizado():
            return self.listaDetallesMuestraSismica[self.posicionActual]
        return None

    def siguiente(self) -> None:
        self.posicionActual += 1