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
        # self.crearCambioEstado(self._estadoActual)

    # Este metodo no deberia usarse
    # Solo se crea para poder crear el setter del Modelo de Dominio
    @property
    def estadoActual(self) -> Estado:
        return self._estadoActual

    # setter del Modelo de Dominio
    @estadoActual.setter
    def estadoActual(self, nuevoEstado: Estado) -> None:
        self._estadoActual = nuevoEstado
        # self.crearCambioEstado(nuevoEstado)

    @property
    def identificadorSismografo(self) -> str:
        return self._identificadorSismografo

    def getNombreEstacionSismologica(self) -> str:
        return self._estacionSismologica.nombre

    # No implementamos un metodo para crear cambios de estado en la clase sismografo
    # ya que no se requiere para el CU23
    # def crearCambioEstado(self, nuevoEstado: Estado) -> None:
    #     pass

    #Métodos de acceso (getters y setters)

    @property
    def fechaAdquisicion(self) -> date:
        return self._fechaAdquisicion
    
    @fechaAdquisicion.setter
    def fechaAdquisicion(self, nuevaFechaAdquisicion: date) -> None:
        self._fechaAdquisicion = nuevaFechaAdquisicion
    
    @identificadorSismografo.setter
    def identificadorSismografo(self, nuevoIdentificadorSismografo: str) -> None:
        self._identificadorSismografo = nuevoIdentificadorSismografo
    
    @property
    def nroSerie(self) -> int:
        return self._nroSerie
    
    @nroSerie.setter
    def nroSerie(self, nuevoNroSerie: int) -> None:
        self._nroSerie = nuevoNroSerie
    
    @estadoActual.setter
    def estadoActual(self, nuevoEstadoActual: Estado) -> None:
        self._estadoActual = nuevoEstadoActual
    
    @property
    def reparaciones(self) -> list[Reparacion]:
        return self._reparaciones
    
    @reparaciones.setter
    def reparaciones(self, nuevaReparaciones: list[Reparacion]) -> None:
        self._reparaciones = nuevaReparaciones
    
    @property
    def seriesTemporales(self) -> list[SerieTemporal]:
        return self._seriesTemporales
    
    @seriesTemporales.setter
    def seriesTemporales(self, nuevaSeriesTemporales: list[SerieTemporal]) -> None:
        self._seriesTemporales = nuevaSeriesTemporales
    
    @property
    def cambiosEstados(self) -> list[CambioEstado]:
        return self._cambiosEstado
    
    @cambiosEstados.setter
    def cambiosEstados(self, nuevoCambiosEstados: list[CambioEstado]) -> None:
        self._cambiosEstado = nuevoCambiosEstados