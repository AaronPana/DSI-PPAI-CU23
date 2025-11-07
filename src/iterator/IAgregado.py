from abc import ABC, abstractmethod
from typing import Generic

from custom_types.iterator import C, T


class IAgregado(
    ABC,
    Generic[C, T],
):
    @abstractmethod
    def crearIterador(self, coleccion: list[C]) -> T:
        pass
