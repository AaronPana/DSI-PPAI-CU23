from iterator.IIterador import IIterador
from entities.SerieTemporal import SerieTemporal
class IteradorSeriesTemporales(IIterador):
    def __init__(self, listaElementos: list[SerieTemporal]):
        self.listaSeriesTemporales: list[SerieTemporal] = listaElementos
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