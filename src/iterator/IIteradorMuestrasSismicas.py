from iterator.IIterador import IIterador
from entities.MuestraSismica import MuestraSismica
class IteradorMuestrasSismicas(IIterador):
    def __init__(self, listaElementos: list[MuestraSismica]):
        self.listaMuestrasSismicas: list[MuestraSismica] = listaElementos
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