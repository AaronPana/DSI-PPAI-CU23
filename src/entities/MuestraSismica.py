from datetime import datetime

from entities.DetalleMuestraSismica import DetalleMuestraSismica

from iterator.IAgregado import IAgregado
from iterator.IIteradorDetallesMuestraSismica import IteradorDetallesMuestraSismica

InfoMuestra = dict[str, str | list[dict[str, str]]]


class MuestraSismica(IAgregado):  # Hereda de IAgregado para el Patron Iterator
    def __init__(self, fechaHoraMuestra: datetime) -> None:
        self._fechaHoraMuestra: datetime = fechaHoraMuestra
        self._detallesMuestraSismica: list[DetalleMuestraSismica] = []

    # Metodos utilizados en el CU23

    # Modificado respecto al Patron Iterador
    def getDatos(self) -> InfoMuestra:
        datosDetalles: list[dict[str, str]] = []

        iteradorDetallesMuestraSismica: IteradorDetallesMuestraSismica = self.crearIterador(self._detallesMuestraSismica)
        iteradorDetallesMuestraSismica.primero()
        while not iteradorDetallesMuestraSismica.haFinalizado():
            detalleMuestraSismicaActual: DetalleMuestraSismica  = iteradorDetallesMuestraSismica.elementoActual()
            if detalleMuestraSismicaActual:
                datosDetalleMuestraSismica = detalleMuestraSismicaActual.getDatos()
                datosDetalles.append(datosDetalleMuestraSismica)
            detalleMuestraSismicaActual.siguiente()

        infoMuestra: InfoMuestra = {
            "fechaHoraMuestra": self._fechaHoraMuestra.strftime("%d/%m/%Y %H:%M:%S"),
            "datosDetalles": datosDetalles,
        }
        return infoMuestra
    
    # Modificado respecto al Patron Iterador
    def crearIterador(listaElementos: list[DetalleMuestraSismica]) -> IteradorDetallesMuestraSismica:
        return IteradorDetallesMuestraSismica(listaElementos)

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
