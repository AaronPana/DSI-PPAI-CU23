from abc import ABC, abstractmethod
from typing import Generic

from custom_types.iterator import T


class IIterador(ABC, Generic[T]):
    @abstractmethod
    def primero(self) -> None:
        pass

    @abstractmethod
    def haFinalizado(self) -> bool:
        pass

    @abstractmethod
    def elementoActual(self) -> T | None:
        pass

    @abstractmethod
    def siguiente(self) -> None:
        pass

    @abstractmethod
    def comprobarFiltro(self) -> bool:
        pass
