from datetime import datetime

from entities.AlcanceSismo import AlcanceSismo
from entities.CambioEstado import CambioEstado
from entities.ClasificacionSismo import ClasificacionSismo
from entities.Empleado import Empleado
from entities.Estado import Estado
from entities.MagnitudRichter import MagnitudRichter
from entities.OrigenDeGeneracion import OrigenDeGeneracion
from entities.SerieTemporal import SerieTemporal

InfoMuestra = dict[str, str | list[dict[str, str]]]
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
        clasificacionSisimo: ClasificacionSismo,
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
        self._clasificacionSisimo: ClasificacionSismo = clasificacionSisimo
        self._magnitud: MagnitudRichter = magnitud
        self._origenDeGeneracion: OrigenDeGeneracion = origenDeGeneracion
        self._alcanceSismo: AlcanceSismo = alcanceSismo
        self._estadoActual: Estado = estadoActual
        self._analistaSupervisor: Empleado = analistaSupervisor
        self._seriesTemporales: list[SerieTemporal] = []
        self._cambiosEstado: list[CambioEstado] = []

    #Metodos utilizados en el CU23

    @property
    def origenDeGeneracion(self) -> str:
        return self._origenDeGeneracion.nombre

    @property
    def clasificacionSisimo(self) -> str:
        return self._clasificacionSisimo.nombre

    @property
    def alcanceSismo(self) -> str:
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
            "fechaHoraOcurrencia": self.fechaHoraOcurrencia.strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "latitudEpicentro": str(self.latitudEpicentro),
            "longitudEpicentro": str(self.longitudEpicentro),
            "latitudHipocentro": str(self.latitudHipocentro),
            "longitudHipocentro": str(self.longitudHipocentro),
            "valorMagnitud": str(self.valorMagnitud),
            "clasificacion": str(self.clasificacionSisimo),
            "origenDeGeneracion": str(self.origenDeGeneracion),
            "alcanceSismico": str(self.alcanceSismo)
        }
        return infoBasicaEventoSismico

    def getDatosEventoSismico(self) -> InfoDatosSismicos:
        """
        rtype: InfoDatosSismicos
        return: diccionario con datos sismicos del evento que
        incluye todos los detalles de todas las muestras de todas las series temporales
        """

        nombreAlcanceSismico = self._alcanceSismo.nombre
        nombreOrigenDeGeneracion = self._origenDeGeneracion.nombre
        nombreClasificacionSismo = self._clasificacionSisimo.nombre

        infoSeriesTemporales: list[InfoSerieTemporal] = self.getDatosSeriesTemporales()

        infoSerieTemporalesOrdenadas: list[InfoSerieTemporal] = (
            self.ordenarSeriesTemporalesPorEstacionSismologica(infoSeriesTemporales)
        )

        infoDatosSismicos: InfoDatosSismicos = {
            "alcanceSismico": nombreAlcanceSismico,
            "origenGeneracion": nombreOrigenDeGeneracion,
            "clasificacion": nombreClasificacionSismo,
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

    def ordenarSeriesTemporalesPorEstacionSismologica(
        self, infoSeriesTemporales: list[InfoSerieTemporal]
    ) -> list[InfoSerieTemporal]:
        return sorted(infoSeriesTemporales, key=lambda x: x["estacionSismologica"])

    def revisar(
        self, nuevoEstado: Estado, responsable: Empleado, fechaHoraInicio: datetime
    ) -> None:
        cambioEstadoActual: CambioEstado = self.buscarCambioEstado()
        cambioEstadoActual.fechaHoraFin = datetime.now()
        self.crearCambioEstado(nuevoEstado, responsable, fechaHoraInicio)

    # La implementacion de revisar() y rechazar() es exactamente la misma debido a que
    # se busca diferenciar los eventos tal cual esta en el diagrama de maquina de estados
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

    #Métodos de acceso (getters y setters)

    @property
    def fechaHoraFin(self) -> datetime:
        return self._fechaHoraFin
    
    @fechaHoraFin.setter
    def fechaHoraFin(self, nuevaFechaHoraFin: datetime) -> None:
        self._fechaHoraFin = nuevaFechaHoraFin

    @fechaHoraOcurrencia.setter
    def fechaHoraOcurrencia(self, nuevaFechaHoraOcurrencia: datetime) -> None:
        self._fechaHoraOcurrencia = nuevaFechaHoraOcurrencia
    
    @latitudEpicentro.setter
    def latitudEpicentro(self, nuevaLatitudEpicentro: float) -> None:
        self._latitudEpicentro = nuevaLatitudEpicentro

    @latitudHipocentro.setter
    def latitudHipocentro(self, nuevaLatitudHipocentro: float) -> None:
        self._latitudHipocentro = nuevaLatitudHipocentro
    
    @longitudEpicentro.setter
    def longitudEpicentro(self, nuevaLongitudEpicentro: float) -> None:
        self._longitudEpicentro = nuevaLongitudEpicentro
    
    @longitudHipocentro.setter
    def longitudHipocentro(self, nuevaLongitudHipocentro: float) -> None:
        self._longitudHipocentro = nuevaLongitudHipocentro
    
    @valorMagnitud.setter
    def valorMagnitud(self, nuevoValorMagnitud: float) -> None:
        self._valorMagnitud = nuevoValorMagnitud

    @clasificacionSisimo.setter
    def clasificacionSisimo(self, nuevaClasificacionSismo: ClasificacionSismo) -> None:
        self._clasificacionSisimo = nuevaClasificacionSismo
    
    @property
    def magnitud(self) -> MagnitudRichter:
        return self._magnitud
    
    @magnitud.setter
    def magnitud(self, nuevaMagnitud: MagnitudRichter) -> None:
        self._magnitud = nuevaMagnitud
    
    @origenDeGeneracion.setter
    def origenDeGeneracion(self, nuevoOrigenDeGeneracion: OrigenDeGeneracion) -> None:
        self._origenDeGeneracion = nuevoOrigenDeGeneracion
    
    @alcanceSismo.setter
    def alcanceSismo(self, nuevoAlcanceSismo: AlcanceSismo) -> None:
        self._alcanceSismo = nuevoAlcanceSismo
    
    @property
    def estadoActual(self) -> Estado:
        return self._estadoActual
    
    @estadoActual.setter
    def estadoActual(self, nuevoEstadoActual: Estado) -> None:
        self._estadoActual = nuevoEstadoActual
    
    @property
    def analistaSupervisor(self) -> Empleado:
        return self._analistaSupervisor
    
    @analistaSupervisor.setter
    def analistaSupervisor(self, nuevoAnalistaSupervisor: Empleado) -> None:
        self._analistaSupervisor = nuevoAnalistaSupervisor
    
    @property
    def seriesTemporales(self) -> list[SerieTemporal]:
        return self._seriesTemporales
    
    @seriesTemporales.setter
    def seriesTemporales(self, nuevaSeriesTemporales: list[SerieTemporal]) -> None:
        self._seriesTemporales = nuevaSeriesTemporales
    
    @property
    def cambiosEstado(self) -> list[CambioEstado]:
        return self._cambiosEstado
    
    @cambiosEstado.setter
    def cambiosEstado(self, nuevoCambioEstado: list[CambioEstado]) -> None:
        self._cambiosEstado = nuevoCambioEstado