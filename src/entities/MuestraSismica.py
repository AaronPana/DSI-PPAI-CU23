from datetime import datetime
from entities.DetalleMuestraSismica import DetalleMuestraSismica

InfoMuestra = dict[str, str | list[dict[str, str]]]


class MuestraSismica:

    def __init__(self, fechaHoraMuestra: datetime) -> None:
        self._fechaHoraMuestra: datetime = fechaHoraMuestra
        self._detallesMuestraSismica: list[DetalleMuestraSismica] = []

    # Metodos utilizados en el CU23

    def getDatos(self) -> InfoMuestra:
        """
        rtype: InfoMuestra
        return: diccionario con fechaHoraMuestra y lista de detalles de la muestra
        """
        datosDetalles: list[dict[str, str]] = [
            detalle.getDatos() for detalle in self._detallesMuestraSismica
        ]

        infoMuestra: InfoMuestra = {
            "fechaHoraMuestra": self._fechaHoraMuestra.strftime("%d/%m/%Y %H:%M:%S"),
            "datosDetalles": datosDetalles,
        }
        return infoMuestra

    # Métodos de acceso (getters y setters)

    @property
    def fechaHoraMuestra(self) -> datetime:
        return self._fechaHoraMuestra

    @fechaHoraMuestra.setter
    def fechaHoraMuestra(self, nuevaFechaHoraMuestra: datetime) -> None:
        self._fechaHoraMuestra = nuevaFechaHoraMuestra

    @property
    def detallesMuestraSismica(self) -> list[DetalleMuestraSismica]:
        return self._detallesMuestraSismica

    @detallesMuestraSismica.setter
    def detallesMuestraSismica(
        self, nuevoDetallesMuestraSismica: list[DetalleMuestraSismica]
    ) -> None:
        self._detallesMuestraSismica = nuevoDetallesMuestraSismica
