# from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from custom_types.sismos import InfoMuestra, InfoSerieTemporal
from entities.Estado import Estado
from entities.MuestraSismica import MuestraSismica
from iterator.IAgregado import IAgregado
from iterator.IIteradorMuestrasSismicas import IteradorMuestrasSismicas

if TYPE_CHECKING:
    from entities.Sismografo import Sismografo


class SerieTemporal(IAgregado[MuestraSismica, IteradorMuestrasSismicas]):
    def __init__(
        self,
        condicionAlarma: bool,
        fechaHoraInicioRegistroMuestras: datetime,
        fechaHoraRegistro: datetime,
        frecuenciaMuestreo: float,
        estado: Estado,
    ) -> None:
        self._condicionAlarma: bool = condicionAlarma
        self._fechaHoraInicioRegistroMuestra: datetime = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro: datetime = fechaHoraRegistro
        self._frecuenciaMuestreo: float = frecuenciaMuestreo
        self._estado: Estado = estado
        self._muestrasSismicas: list[MuestraSismica] = []

    # Metodos utilizados en el CU23

    # Modificado respecto al Patron Iterador
    def getDatos(self, sismografos: list["Sismografo"]) -> InfoSerieTemporal:
        datosMuestras: list[InfoMuestra] = []
        sismografo: Sismografo = self.esMiSismografo(sismografos)

        iteradorMuestrasSismicas: IteradorMuestrasSismicas = self.crearIterador(
            self._muestrasSismicas
        )
        iteradorMuestrasSismicas.primero()
        while not iteradorMuestrasSismicas.haFinalizado():
            muestraSismicaActual: MuestraSismica | None = (
                iteradorMuestrasSismicas.elementoActual()
            )
            if muestraSismicaActual:
                datoMuestraSismica: InfoMuestra = muestraSismicaActual.getDatos()
                datosMuestras.append(datoMuestraSismica)
            iteradorMuestrasSismicas.siguiente()

        infoSerieTemporal: InfoSerieTemporal = {
            "estacionSismologica": sismografo.getNombreEstacionSismologica(),
            "fechaHoraRegistro": self._fechaHoraRegistro.strftime("%d/%m/%Y %H:%M:%S"),
            "frecuenciaMuestreo": str(self._frecuenciaMuestreo),
            "condicionAlarma": "SI" if self._condicionAlarma else "NO",
            "datosMuestras": datosMuestras,
        }
        return infoSerieTemporal

    # Modificado respecto al Patron Iterador
    def crearIterador(
        self, coleccion: list[MuestraSismica]
    ) -> IteradorMuestrasSismicas:
        return IteradorMuestrasSismicas(coleccion)

    def esMiSismografo(self, sismografos: list["Sismografo"]) -> "Sismografo":
        return [sismografo for sismografo in sismografos if sismografo.esMiSerie(self)][
            0
        ]

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
    def frecuenciaMuestreo(self) -> float:
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
        self._sismografo: Sismografo = nuevoSismografo

    @property
    def muestrasSismicas(self) -> list[MuestraSismica]:
        return self._muestrasSismicas

    @muestrasSismicas.setter
    def muestrasSismicas(self, nuevaMuestrasSismicas: list[MuestraSismica]) -> None:
        self._muestrasSismicas = nuevaMuestrasSismicas
