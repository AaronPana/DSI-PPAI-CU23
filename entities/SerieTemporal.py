from datetime import datetime
from entities.Estado import Estado
from entities.MuestraSismica import MuestraSismica

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.Sismografo import Sismografo

InfoMuestra = dict[str, str | list[dict[str, str]]]
InfoSerieTemporal = dict[str, str | list[InfoMuestra]]


class SerieTemporal:

    def __init__(
        self,
        condicionAlarma: bool,
        fechaHoraInicioRegistroMuestras: datetime,
        fechaHoraRegistro: datetime,
        frecuenciaMuestreo: int,
        estado: Estado,
        sismografo: "Sismografo",
    ) -> None:
        self._condicionAlarma: bool = condicionAlarma
        self._fechaHoraInicioRegistroMuestra: datetime = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro: datetime = fechaHoraRegistro
        self._frecuenciaMuestreo: int = frecuenciaMuestreo
        self._estado: Estado = estado
        self._sismografo: "Sismografo" = sismografo
        self._muestrasSismicas: list[MuestraSismica] = []

    # Metodos utilizados en el CU23

    def getDatos(self) -> InfoSerieTemporal:
        """
        rtype: InfoSerieTemporal
        return: diccionario con datos y lista de muestras de la serie temporal
        """
        datosMuestras: list[InfoMuestra] = [
            muestra.getDatos() for muestra in self._muestrasSismicas
        ]

        infoSerieTemporal: InfoSerieTemporal = {
            "estacionSismologica": self._sismografo.getNombreEstacionSismologica(), #metodo sismografo referencia - esto es relacion de atributo no dependencia
            "fechaHoraRegistro": self._fechaHoraRegistro.strftime("%d/%m/%Y %H:%M:%S"), 
            "frecuenciaMuestreo": str(self._frecuenciaMuestreo),
            "condicionAlarma": "SI" if self._condicionAlarma else "NO",
            "datosMuestras": datosMuestras,
        }

        return infoSerieTemporal

    # Métodos de acceso (getters y setters)

    @property
    def condicionAlarma(self) -> bool:
        return self._condicionAlarma

    @condicionAlarma.setter
    def condicionAlarma(self, nuevaCondicionAlarma: bool) -> None:
        self._condicionAlarma = nuevaCondicionAlarma

    @property
    def fechaHoraInicioRegistroMuestra(self) -> datetime:
        return self._fechaHoraInicioRegistroMuestra

    @fechaHoraInicioRegistroMuestra.setter
    def fechaHoraInicioRegistroMuestra(
        self, nuevaFechaHoraInicioRegistroMuestra: datetime
    ) -> None:
        self._fechaHoraInicioRegistroMuestra = nuevaFechaHoraInicioRegistroMuestra

    @property
    def fechaHoraRegistro(self) -> datetime:
        return self._fechaHoraRegistro

    @fechaHoraRegistro.setter
    def fechaHoraRegistro(self, nuevaFechaHoraRegistro: datetime) -> None:
        self._fechaHoraRegistro = nuevaFechaHoraRegistro

    @property
    def frecuenciaMuestreo(self) -> int:
        return self._frecuenciaMuestreo

    @frecuenciaMuestreo.setter
    def frecuenciaMuestreo(self, nuevaFrecuenciaMuestreo: int) -> None:
        self._frecuenciaMuestreo = nuevaFrecuenciaMuestreo

    @property
    def estado(self) -> Estado:
        return self._estado

    @estado.setter
    def estado(self, nuevoEstado: Estado) -> None:
        self._estado = nuevoEstado

    @property
    def sismografo(self) -> "Sismografo":
        return self._sismografo

    @sismografo.setter
    def sismografo(self, nuevoSismografo: "Sismografo") -> None:
        self._sismografo = nuevoSismografo

    @property
    def muestrasSismicas(self) -> list[MuestraSismica]:
        return self._muestrasSismicas

    @muestrasSismicas.setter
    def muestrasSismicas(self, nuevaMuestrasSismicas: list[MuestraSismica]) -> None:
        self._muestrasSismicas = nuevaMuestrasSismicas
