from abc import ABC, abstractmethod
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
