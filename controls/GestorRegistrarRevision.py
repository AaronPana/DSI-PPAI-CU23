from datetime import datetime
from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision
from entities.Estado import Estado
from entities.EventoSismico import EventoSismico


class GestorRegistrarRevision:
    def __init__(
        self,
        boundaryRegistrarRevision: BoundaryRegistrarRevision,
        fechaHoraActual: datetime,
    ) -> None:
        self._fechaHoraActual: datetime = fechaHoraActual
        self._boundaryRegistrarRevision: BoundaryRegistrarRevision = (
            boundaryRegistrarRevision
        )
        # Deben obtenerse al crear el gestor
        # a traves del metodo "obtenerEventoSismicoNoRevisado()"
        self._eventosSismicosNoRevisados: list[EventoSismico] = []
        # Debe asignarse cuando sea seleccionado
        self._eventoSismicoSeleccionado: EventoSismico | None = None
        # Debe asignarse caundo se llama al metodo "buscarDetalleEventoSismico()"
        self._datosEventoSismico: None = None
        # Debe asignarse caundo se llama al metodo "buscarDetalleEventoSismico()"
        self._datosSerieTemporal: None = None
        # Debe asignarse cuando se llama al metodo "generarSismograma()"
        self._sismograma: None = None
        # Debería asignarse cuando se llama al metodo "cambiarEstadoEventoSismico()"
        self._estadoEvento: Estado | None = None
        self._tieneDatosValidosEventoSismico: bool = False

    def seleccionDatosEventosSismicos(self):
        pass

    def obtenerEventoSismicoNoRevisado(self):
        pass

    def ordenarPorFechaHoraOcurrencia(self):
        pass

    def seleccionEventoSismico(self):
        pass

    def cambiarEstadoEventoSismico(self):
        pass

    def buscarSesion(self):
        pass

    def getFechaHora(self) -> datetime:
        return datetime.now()

    def buscarDetalleEventoSismico(self):
        pass

    def generarSismograma(self):
        pass

    def tomarSeleccionRevision(self):
        pass

    def validarDatosEventoSismico(self):
        pass

    def finCasoUso(self):
        pass
