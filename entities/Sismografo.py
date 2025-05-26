from datetime import date

from entities.CambioEstado import CambioEstado
from entities.EstacionSismologica import EstacionSismologica
from entities.Estado import Estado
from entities.ModeloSismografo import ModeloSismografo
from entities.Reparacion import Reparacion
from entities.SerieTemporal import SerieTemporal


class Sismografo:

    def __init__(
        self,
        fechaAdquisicion: date,
        identificadorSismografo: str,
        nroSerie: int,
        estacionSismologica: EstacionSismologica,
        estadoActual: Estado,
        modeloSismografo: ModeloSismografo,
    ) -> None:
        self._fechaAdquisicion: date = fechaAdquisicion
        self._identificadorSismografo: str = identificadorSismografo
        self._nroSerie: int = nroSerie
        self._estacionSismologica: EstacionSismologica = estacionSismologica
        self._estadoActual: Estado = estadoActual
        self._modeloSismografo: ModeloSismografo = modeloSismografo
        # No implementamos un metodo para asociar reparaciones ya que no se requiere para el CU23
        self._reparaciones: list[Reparacion] = []
        # Como debería implementarse la lógica de asociación ??
        self._seriesTemporales: list[SerieTemporal] = []
        # No deberia recibir los cambios de estado sino irlos creando y asignando los estados
        self._cambiosEstado: list[CambioEstado] = []
        # Primer cambio de estado
        self.crearCambioEstado(self._estadoActual)

    # Este metodo no deberia usarse
    # Solo se crea para poder crear el setter del Modelo de Dominio
    @property
    def estadoActual(self) -> Estado:
        return self._estadoActual

    # setter del Modelo de Dominio
    @estadoActual.setter
    def estadoActual(self, nuevoEstado: Estado) -> None:
        self._estadoActual = nuevoEstado
        self.crearCambioEstado(nuevoEstado)

    @property
    def identificadorSismografo(self) -> str:
        return self._identificadorSismografo

    def getNombreEstacion(self) -> str:
        return self._estacionSismologica.nombre

    def crearCambioEstado(self, nuevoEstado: Estado) -> None:
        pass
