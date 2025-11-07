from entities.DetalleMuestraSismica import DetalleMuestraSismica
from iterator.IIterador import IIterador


class IteradorDetallesMuestraSismica(IIterador[DetalleMuestraSismica]):
    def __init__(self, listaElementos: list[DetalleMuestraSismica]) -> None:
        self.listaDetallesMuestraSismica: list[DetalleMuestraSismica] = listaElementos
        self.posicionActual: int = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaDetallesMuestraSismica)

    def elementoActual(self) -> DetalleMuestraSismica | None:
        if not self.haFinalizado():
            return self.listaDetallesMuestraSismica[self.posicionActual]
        return None

    def comprobarFiltro(self) -> bool:
        return False

    def siguiente(self) -> None:
        self.posicionActual += 1
