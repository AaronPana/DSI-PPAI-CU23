from iterator.IIterador import IIterador
from entities.DetalleMuestraSismica import DetalleMuestraSismica
class IteradorDetallesMuestraSismica(IIterador):
    def __init__(self, listaElementos: list[DetalleMuestraSismica]):
        self.listaDetallesMuestraSismica: list[DetalleMuestraSismica] = listaElementos
        self.posicionActual: int = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaDetallesMuestraSismica)

    def elementoActual(self) -> object:
        if not self.haFinalizado():
            return self.listaDetallesMuestraSismica[self.posicionActual]
        return None
    
    def comprobarFiltro(self):
        pass

    def siguiente(self) -> None:
        self.posicionActual += 1