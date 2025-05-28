from datetime import datetime
from entities.DetalleMuestraSismica import DetalleMuestraSismica


InfoMuestra = dict[str, str | list[str]]


class MuestraSismica:

    def __init__(self, fechaHoraMuestra: datetime) -> None:
        self._fechaHoraMuestra: datetime = fechaHoraMuestra
        self._detallesMuestraSismica: list[DetalleMuestraSismica] = []

    def getDatos(self) -> InfoMuestra:
        """
        rtype: InfoMuestra
        return: diccionario con fechaHoraMuestra y lista de detalles de la muestra
        """
        datosDetalles: list[str] = [
            detalle.getDatos() for detalle in self._detallesMuestraSismica
        ]

        infoMuestra: InfoMuestra = {
            "fechaHoraMuestra": self._fechaHoraMuestra.strftime("%d/%m/%Y %H:%M:%S"),
            "datosDetalles": datosDetalles,
        }

        return infoMuestra
