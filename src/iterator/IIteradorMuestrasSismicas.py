from entities.MuestraSismica import MuestraSismica
from iterator.IIterador import IIterador


class IteradorMuestrasSismicas(IIterador[MuestraSismica]):
    def __init__(self, listaElementos: list[MuestraSismica]) -> None:
        self.listaMuestrasSismicas: list[MuestraSismica] = listaElementos
        self.posicionActual: int = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaMuestrasSismicas)

    def elementoActual(self) -> MuestraSismica | None:
        if not self.haFinalizado():
            return self.listaMuestrasSismicas[self.posicionActual]
        return None

    def comprobarFiltro(self) -> bool:
        return False

    def siguiente(self) -> None:
        self.posicionActual += 1
