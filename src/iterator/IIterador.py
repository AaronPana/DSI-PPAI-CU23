from abc import ABC, abstractmethod

# + new(listaElementos: object[]): Iterador
# + primero(): None
# + haFinalizado(): bool
# + elementoActual(): object
# + comprobarFiltro(): bool
# + siguiente(): None

class IIterador(ABC):
    @abstractmethod
    def primero(self) -> None:
        pass

    @abstractmethod
    def haFinalizado(self) -> bool:
        pass

    @abstractmethod
    def elementoActual(self) -> object:
        pass

    @abstractmethod
    def siguiente(self) -> None:
        pass

    @abstractmethod
    def comprobarFiltro(self) -> bool:
        pass
