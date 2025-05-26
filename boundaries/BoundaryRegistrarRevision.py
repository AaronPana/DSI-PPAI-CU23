from datetime import datetime
from controls.GestorRegistrarRevision import GestorRegistrarRevision


class BoundaryRegistrarRevision:

    def __init__(self) -> None:
        self._gestorRegistrarRevision: GestorRegistrarRevision = (
            GestorRegistrarRevision(self, datetime.now())
        )
        self._grillaEventosSismicosNoRevisados = None
        self._btnSeleccionarEventoSismicoNoRevisado = None
        self._grillaEventoSismicoSeleccionado = None
        self._btnVisualizarMapa = None
        self._btnModificarDatosEventoSismico = None
        self._campoAccionRevision = None

    def registrarRevisionManual(self):
        pass

    def habilitarVentana(self):
        pass

    def mostrarDatosEventosSismicos(self):
        pass

    def seleccionEventoSismico(self):
        pass

    def mostrarDatosEventoSismico(self):
        pass

    def mostrarSismograma(self):
        pass

    def habilitarOpcionVisualizarMapa(self):
        pass

    def habilitarBtnMapa(self):
        pass

    def habilitarModificarDatosEventoSismico(self):
        pass

    def solicitarAccionRevision(self):
        pass

    def tomarSeleccionRevision(self):
        pass
