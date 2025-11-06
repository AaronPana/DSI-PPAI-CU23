from entities.EventoSismico import EventoSismico
from iterator.IIterador import IIterador


class IteradorEventosSismicos(IIterador[EventoSismico]):
    def __init__(self, listaElementos: list[EventoSismico]) -> None:
        self.listaEventosSismicos: list[EventoSismico] = listaElementos
        self.posicionActual = 0

    def primero(self) -> None:
        self.posicionActual = 0

    def haFinalizado(self) -> bool:
        return self.posicionActual >= len(self.listaEventosSismicos)

    def elementoActual(self) -> EventoSismico | None:
        if not self.haFinalizado():
            return self.listaEventosSismicos[self.posicionActual]
        return None

    def comprobarFiltro(self) -> bool:
        evento: EventoSismico | None = self.elementoActual()
        if not evento:
            return False
        return evento.esAutoDetectado() or evento.esPendienteRevision()

    def siguiente(self) -> None:
        self.posicionActual += 1
