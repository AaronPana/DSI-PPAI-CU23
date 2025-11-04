from .IIterador import IIterador
from typing import List
from entities.EventoSismico import EventoSismico

# IIteradorEventosSismicos
# - listaEventosSismicos: EventoSismico[]
# - posicionActual: int
# + new(listaElementos: object[]): Iterador
# + primero(): None
# + haFinalizado(): bool
# + elementoActual(): object
# + comprobarFiltro(): bool
# + siguiente(): None

class IteradorEventosSismicos(IIterador):
    def __init__(self, listaElementos: List[EventoSismico]):
        self.listaEventosSismicos:List[EventoSismico] = listaElementos
        self.posicionActual = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaEventosSismicos)

    def elementoActual(self) -> object:
        if not self.haFinalizado():
            return self.listaEventosSismicos[self.posicionActual]
        return None

    def comprobarFiltro(self) -> bool:
        evento = self.elementoActual()
        if evento is None:
            return False
        return evento.esAutoDetectado() or evento.esPendienteRevision()


    def siguiente(self) -> None:
        self.posicionActual += 1