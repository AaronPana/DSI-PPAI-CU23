from datetime import datetime

from entities.AlcanceSismo import AlcanceSismo
from entities.CambioEstado import CambioEstado
from entities.ClasificacionSismo import ClasificacionSismo
from entities.Empleado import Empleado
from entities.Estado import Estado
from entities.MagnitudRichter import MagnitudRichter
from entities.OrigenDeGeneracion import OrigenDeGeneracion
from entities.SerieTemporal import SerieTemporal


class EventoSismico:

    def __init__(
        self,
        fechaHoraFin: datetime,
        fechaHoraOcurrencia: datetime,
        latitudEpicentro: str,
        latitudHipocentro: str,
        longitudEpicentro: str,
        longitudHipocentro: str,
        valorMagnitud: float,
        clasificacion: ClasificacionSismo,
        magnitud: MagnitudRichter,
        origenDeGeneracion: OrigenDeGeneracion,
        alcanceSismo: AlcanceSismo,
        estadoActual: Estado,
        analistaSupervisor: Empleado,
    ) -> None:
        self._fechaHoraFin: datetime = fechaHoraFin
        self._fechaHoraOcurrencia: datetime = fechaHoraOcurrencia
        self._latitudEpicentro: str = latitudEpicentro
        self._latitudHipocentro: str = latitudHipocentro
        self._longitudEpicentro: str = longitudEpicentro
        self._longitudHipocentro: str = longitudHipocentro
        self._valorMagnitud: float = valorMagnitud
        self._clasificacion: ClasificacionSismo = clasificacion
        self._magnitud: MagnitudRichter = magnitud
        self._origenDeGeneracion: OrigenDeGeneracion = origenDeGeneracion
        self._alcanceSismo: AlcanceSismo = alcanceSismo
        self._estadoActual: Estado = estadoActual
        self._analistaSupervisor: Empleado = analistaSupervisor
        # Como debería implementarse la lógica de asociación ??
        self._seriesTemporales: list[SerieTemporal] = []
        # No deberia recibir los cambios de estado sino irlos creando y asignando los estados
        self._cambiosEstado: list[CambioEstado] = []
        # Primer cambio de estado
        self.crearCambioEstado(self._estadoActual)

    @property
    def origenDeGeneracion(self) -> str:
        return self._origenDeGeneracion.nombre

    @property
    def clasificacion(self) -> str:
        return self._clasificacion.nombre

    @property
    def alcanceSismico(self) -> str:
        return self._alcanceSismo.nombre

    @property
    def valorMagnitud(self) -> float:
        return self._valorMagnitud

    @property
    def fechaHoraOcurrencia(self) -> datetime:
        return self._fechaHoraOcurrencia

    @property
    def latitudEpicentro(self) -> str:
        return self._latitudEpicentro

    @property
    def latitudHipocentro(self) -> str:
        return self._latitudHipocentro

    @property
    def longitudEpicentro(self) -> str:
        return self._longitudEpicentro

    @property
    def longitudHipocentro(self) -> str:
        return self._longitudHipocentro

    def getDatos(self):
        pass

    def getDatosSismicos(self):
        pass

    def getDatoSeriesTemporales(self):
        pass

    def esAutoDetectado(self):
        pass

    def esPendienteRevision(self):
        pass

    def revisar(self):
        pass

    def buscarCambioEstado(self):
        pass

    def crearCambioEstado(self, nuevoEstado: Estado) -> None:
        pass

    def ordenarSeriesTemporalesPorEstacion(self):
        pass

    def rechazar(self):
        pass
