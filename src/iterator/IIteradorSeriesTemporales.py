from entities.SerieTemporal import SerieTemporal
from iterator.IIterador import IIterador


class IteradorSeriesTemporales(IIterador[SerieTemporal]):
    def __init__(self, listaElementos: list[SerieTemporal]) -> None:
        self.listaSeriesTemporales: list[SerieTemporal] = listaElementos
        self.posicionActual = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaSeriesTemporales)

    def elementoActual(self) -> SerieTemporal | None:
        if not self.haFinalizado():
            return self.listaSeriesTemporales[self.posicionActual]
        return None

    def comprobarFiltro(self) -> bool:
        return False

    def siguiente(self) -> None:
        self.posicionActual += 1
