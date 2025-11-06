from iterator.IIterador import IIterador
from entities.EventoSismico import EventoSismico
class IteradorEventosSismicos(IIterador):
    def __init__(self, listaElementos: list[EventoSismico]):
        self.listaEventosSismicos:list[EventoSismico] = listaElementos
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
        evento: EventoSismico = self.elementoActual()
        if evento is None:
            return False
        return evento.esAutoDetectado() or evento.esPendienteRevision()


    def siguiente(self) -> None:
        self.posicionActual += 1