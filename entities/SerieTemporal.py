from datetime import datetime
from entities.Estado import Estado
from entities.MuestraSismica import MuestraSismica


class SerieTemporal:

    def __init__(
        self,
        condicionAlarma: str,
        fechaHoraInicioRegistroMuestras: datetime,
        fechaHoraRegistro: datetime,
        frecuenciaMuestreo: int,
        estado: Estado,
    ) -> None:
        self._condicionAlarma: str = condicionAlarma
        self._fechaHoraInicioRegistroMuestra: datetime = fechaHoraInicioRegistroMuestras
        self._fechaHoraRegistro: datetime = fechaHoraRegistro
        self._frecuenciaMuestreo: int = frecuenciaMuestreo
        self._estado: Estado = estado
        self._muestrasSismicas: list[MuestraSismica] = []

    def getDatos(self):
        pass

    # Acá se implementa la lógica de creación de muestras
    # y se agregan a al atributo "_muestrasSismicas"
    def crearMuestraSismica(self):
        pass

    def esSerieTemporalDeEvento(self):
        pass
