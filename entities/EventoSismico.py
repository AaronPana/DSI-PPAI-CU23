from datetime import datetime

from entities.AlcanceSismo import AlcanceSismo
from entities.CambioEstado import CambioEstado
from entities.ClasificacionSismo import ClasificacionSismo
from entities.Empleado import Empleado
from entities.Estado import Estado
from entities.MagnitudRichter import MagnitudRichter
from entities.OrigenDeGeneracion import OrigenDeGeneracion
from entities.SerieTemporal import SerieTemporal


InfoMuestra = dict[str, str | list[str]]
InfoSerieTemporal = dict[str, str | list[InfoMuestra]]
InfoDatosSismicos = dict[str, str | list[InfoSerieTemporal]]


class EventoSismico:

    def __init__(
        self,
        fechaHoraFin: datetime,
        fechaHoraOcurrencia: datetime,
        latitudEpicentro: float,
        latitudHipocentro: float,
        longitudEpicentro: float,
        longitudHipocentro: float,
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
        self._latitudEpicentro: float = latitudEpicentro
        self._latitudHipocentro: float = latitudHipocentro
        self._longitudEpicentro: float = longitudEpicentro
        self._longitudHipocentro: float = longitudHipocentro
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
        # self.crearCambioEstado(self._estadoActual)

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
    def latitudEpicentro(self) -> float:
        return self._latitudEpicentro

    @property
    def longitudEpicentro(self) -> float:
        return self._longitudEpicentro

    @property
    def latitudHipocentro(self) -> float:
        return self._latitudHipocentro

    @property
    def longitudHipocentro(self) -> float:
        return self._longitudHipocentro

    def esAutoDetectado(self) -> bool:
        return self._estadoActual.esAutoDetectado()

    def esPendienteRevision(self) -> bool:
        return self._estadoActual.esPendienteRevision()

    def getDatos(self) -> dict[str, str]:
        """
        rtype: dict[str, str]
        return: diccionarios de datos basicos del evento sismico
        """
        infoBasicaEventoSismico: dict[str, str] = {
            "fechaHoraOcurrencia": self._fechaHoraOcurrencia.strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "latitudEpicentro": str(self._latitudEpicentro),
            "longitudEpicentro": str(self._longitudEpicentro),
            "latitudHipocentro": str(self._latitudHipocentro),
            "longitudHipocentro": str(self._longitudHipocentro),
            "valorMagnitud": str(self._valorMagnitud),
        }
        return infoBasicaEventoSismico

    def getDatosSismicos(self) -> InfoDatosSismicos:
        """
        rtype: InfoDatosSismicos
        return: diccionario con datos sismicos del evento que
        incluye todos los detalles de todas las muestras de todas las series temporales
        """

        infoSeriesTemporales: list[InfoSerieTemporal] = self.getDatosSeriesTemporales()

        infoSerieTemporalesOrdenadas: list[InfoSerieTemporal] = (
            self.ordenarSeriesTemporalesPorEstacion(infoSeriesTemporales)
        )

        infoDatosSismicos: InfoDatosSismicos = {
            "alcanceSismico": self._alcanceSismo.nombre,
            "origenGeneracion": self._origenDeGeneracion.nombre,
            "clasificacion": self._clasificacion.nombre,
            "infoSeriesTemporales": infoSerieTemporalesOrdenadas,
        }
        return infoDatosSismicos

    def getDatosSeriesTemporales(self) -> list[InfoSerieTemporal]:
        """
        rtype: list[InfoSerieTemporal]
        return: diccionario con todos los detalles de todas las muestras de todas las series temporales
        """
        infoSeriesTemporales: list[InfoSerieTemporal] = [
            serie.getDatos() for serie in self._seriesTemporales
        ]
        return infoSeriesTemporales

    def ordenarSeriesTemporalesPorEstacion(
        self, infoSeriesTemporales: list[InfoSerieTemporal]
    ) -> list[InfoSerieTemporal]:
        return sorted(infoSeriesTemporales, key=lambda x: x["estacionSismologica"])

    def revisar(
        self, nuevoEstado: Estado, responsable: Empleado, fechaHoraInicio: datetime
    ) -> None:
        cambioEstadoActual: CambioEstado = self.buscarCambioEstado()
        cambioEstadoActual.fechaHoraFin = datetime.now()
        self.crearCambioEstado(nuevoEstado, responsable, fechaHoraInicio)

    # La implementacion de revisar() y rechazar() es exactamente la msima debido a que
    # se busca diferenciar los eventos tal cual esta en la maquia de estados
    def rechazar(
        self, nuevoEstado: Estado, responsable: Empleado, fechaHoraInicio: datetime
    ) -> None:
        cambioEstadoActual: CambioEstado = self.buscarCambioEstado()
        cambioEstadoActual.fechaHoraFin = datetime.now()
        self.crearCambioEstado(nuevoEstado, responsable, fechaHoraInicio)

    def buscarCambioEstado(self) -> CambioEstado:
        cambioEstadoActual: CambioEstado = [
            cambio for cambio in self._cambiosEstado if cambio.esEstadoActual()
        ][0]
        return cambioEstadoActual

    def crearCambioEstado(
        self, nuevoEstado: Estado, responsable: Empleado, fechaHoraInicio: datetime
    ) -> None:
        nuevoCambioEstado: CambioEstado = CambioEstado(
            nuevoEstado, responsable, fechaHoraInicio
        )
        self._cambiosEstado.append(nuevoCambioEstado)
