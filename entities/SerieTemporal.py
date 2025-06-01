from datetime import datetime
from entities.Estado import Estado
from entities.MuestraSismica import MuestraSismica
from entities.Sismografo import Sismografo


InfoMuestra = dict[str, str | list[str]]
InfoSerieTemporal = dict[str, str | list[InfoMuestra]]


class SerieTemporal:

    def __init__(
        self,
        condicionAlarma: bool,
        fechaHoraInicioRegistroMuestras: datetime,
        fechaHoraRegistro: datetime,
        frecuenciaMuestreo: int,
        estado: Estado,
        sismografo: Sismografo,
    ) -> None:
        self._condicionAlarma: bool = condicionAlarma
        self._fechaHoraInicioRegistroMuestra: datetime = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro: datetime = fechaHoraRegistro
        self._frecuenciaMuestreo: int = frecuenciaMuestreo
        self._estado: Estado = estado
        self._sismografo: Sismografo = sismografo
        self._muestrasSismicas: list[MuestraSismica] = []

    def getDatos(self) -> InfoSerieTemporal:
        """
        rtype: InfoSerieTemporal
        return: diccionario con datos y lista de muestras de la serie temporal
        """
        datosMuestras: list[InfoMuestra] = [
            muestra.getDatos() for muestra in self._muestrasSismicas
        ]

        infoSerieTemporal: InfoSerieTemporal = {
            "estacionSismologica": self._sismografo.getNombreEstacion(),
            "fechaHoraRegistro": self._fechaHoraRegistro.strftime("%d/%m/%Y %H:%M:%S"),
            "frecuenciaMuestreo": str(self._frecuenciaMuestreo),
            "condicionAlarma": "SI" if self._condicionAlarma else "NO",
            "datosMuestras": datosMuestras,
        }

        return infoSerieTemporal
