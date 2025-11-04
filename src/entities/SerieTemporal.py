# from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from entities.Estado import Estado
from entities.MuestraSismica import MuestraSismica

from iterator.IAgregado import IAgregado
from iterator.IIteradorMuestrasSismicas import IteradorMuestrasSismicas

if TYPE_CHECKING:
    from entities.Sismografo import Sismografo

InfoMuestra = dict[str, str | list[dict[str, str]]]
InfoSerieTemporal = dict[str, str | list[InfoMuestra]]


class SerieTemporal(IAgregado):  # Hereda de IAgregado para el Patron Iterator
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
        sismografo: Sismografo = self.esMiSismografo(sismografos) #FALTA ESTO EN EL DIAGRAMA DE SECUENCIA

        iteradorMuestrasSismicas: IteradorMuestrasSismicas = self.crearIterador(self._muestrasSismicas) #ESTO SE LLAMA NEW, CAMBIAR NOMBRE POR crearIterador()
        iteradorMuestrasSismicas.primero()
        while not iteradorMuestrasSismicas.haFinalizado():
            muestraSismicaActual: MuestraSismica  = iteradorMuestrasSismicas.elementoActual()
            if muestraSismicaActual:
                datoMuestraSismica = muestraSismicaActual.getDatos()
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
    def crearIterador(self, listaElementos: list[MuestraSismica]) -> IteradorMuestrasSismicas:
        return IteradorMuestrasSismicas(listaElementos)

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
