from datetime import datetime

from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision
from controllers.GestorGenerarSismograma import GestorGenerarSismograma
from data.estados import estado_data
from data.eventosSismicos import eventoSismico_data
from data.sesiones import Sesion0
from data.sismografos import sismografo_data

from entities.Empleado import Empleado
from entities.Estado import Estado
from entities.EventoSismico import EventoSismico
from entities.Sesion import Sesion
from entities.Sismografo import Sismografo

from iterator.IAgregado import IAgregado
from iterator.IIteradorEventosSismicos import IteradorEventosSismicos

InfoMuestra = dict[str, str | list[dict[str, str]]]
InfoSerieTemporal = dict[str, str | list[InfoMuestra]]
InfoDatosSismicos = dict[str, str | list[InfoSerieTemporal]]


class GestorRegistrarRevision(IAgregado): #Hereda de IAgregado para el Patron Iterator
    def __init__(
        self,
        boundaryRegistrarRevision: BoundaryRegistrarRevision,
        fechaHoraActual: datetime,
    ) -> None:
        self._boundaryRegistrarRevision: BoundaryRegistrarRevision = (
            boundaryRegistrarRevision
        )
        self._fechaHoraActual: datetime = fechaHoraActual
        self._sesion: Sesion = Sesion0

        self._sismografos: list[Sismografo] = sismografo_data
        self._eventos: list[EventoSismico] = eventoSismico_data
        self._eventosSismicosNoRevisados: list[EventoSismico] = []
        self._datosEventosSismicosNoRevisados: list[dict[str, str]] = []
        self._eventoSismicoSeleccionado: EventoSismico | None = None
        self._datosEventoSismico: InfoDatosSismicos | None = None

        self._estados: list[Estado] = estado_data
        self._estadoEvento: Estado | None = None

        self._responsable: Empleado | None = None

        self._sismograma: str | None = None

        self._accionesRevision: list[str] = [
            "CONFIRMAR",
            "RECHAZAR",
            "SOLICITAR REVISION",
        ]

        self._tieneDatosValidos: bool = False

    def seleccionDatosEventosSismicos(self) -> None:
        self.obtenerEventosSismicosNoRevisados()
        self.ordenarPorFechaHoraOcurrencia()
        self._boundaryRegistrarRevision.mostrarDatosEventosSismicos(
            self._datosEventosSismicosNoRevisados
        )
    
    # Modificado respecto al Patron Iterador
    def obtenerEventosSismicosNoRevisados(self) -> None:
        iteradorEventosSismicos: IteradorEventosSismicos = self.crearIterador(self._eventos)
        iteradorEventosSismicos.primero()

        while not iteradorEventosSismicos.haFinalizado():
            if iteradorEventosSismicos.comprobarFiltro():
                evento: EventoSismico = iteradorEventosSismicos.elementoActual()
                if evento is not None:
                    self._eventosSismicosNoRevisados.append(evento)
                    self._datosEventosSismicosNoRevisados.append(evento.getDatos())
            iteradorEventosSismicos.siguiente()

    def crearIterador(self, listaElementos: list[EventoSismico]) -> IteradorEventosSismicos:
        return IteradorEventosSismicos(listaElementos)

    def ordenarPorFechaHoraOcurrencia(self) -> None:
        self._eventosSismicosNoRevisados.sort(
            key=lambda evento: evento.fechaHoraOcurrencia
        )
        self._datosEventosSismicosNoRevisados.sort(
            key=lambda evento: datetime.strptime(
                evento["fechaHoraOcurrencia"], "%d/%m/%Y %H:%M:%S"
            )
        )

    def seleccionEventoSismico(self, eventoDict: dict[str, str]) -> None:
        # Este proceso de busqueda esta implementado de tal forma que se respete que
        # el boundary no conozca objetos "entity" y a su vez que el gestor si maneje estos objetos
        for evento in self._eventosSismicosNoRevisados:
            if (
                str(evento.latitudEpicentro) == eventoDict["latitudEpicentro"]
                and str(evento.longitudEpicentro) == eventoDict["longitudEpicentro"]
                and str(evento.latitudHipocentro) == eventoDict["latitudHipocentro"]
                and str(evento.longitudHipocentro) == eventoDict["longitudHipocentro"]
                and str(evento.valorMagnitud) == eventoDict["valorMagnitud"]
            ):
                self._eventoSismicoSeleccionado = evento
        self.revisarEventoSismico()
        self.buscarDetalleEventoSismico()
        self.generarSismograma()

        self._boundaryRegistrarRevision.mostrarDatosEventoSismico(
            self._datosEventoSismico
        )
        self._boundaryRegistrarRevision.mostrarSismograma(self._sismograma)
        self._boundaryRegistrarRevision.habilitarOpcionVisualizarMapa(True)
        self._boundaryRegistrarRevision.habilitarModificarDatosEventoSismico(True)
        self._boundaryRegistrarRevision.solicitarAccionRevision()

    def revisarEventoSismico(self) -> None:
        nuevoEstado: Estado = [
            estado
            for estado in self._estados
            if estado.esAmbitoEventoSismico() and estado.esBloqueadoEnRevision()
        ][0]

        self._responsable = self.buscarUsuario()

        fechaHoraActual: datetime = self.getFechaHora()

        if self._eventoSismicoSeleccionado is not None:
            self._eventoSismicoSeleccionado.revisar(
                nuevoEstado, self._responsable, fechaHoraActual
            )

    # La implementacion de revisarEventoSismico() y rechazarEventoSismico() es casi la misma debido a que
    # se busca diferenciar los eventos tal cual esta en la maquia de estados
    # En este caso ya no es necesario busacr el responsable
    def rechazarEventoSismico(self) -> bool:
        nuevoEstado: Estado = [
            estado
            for estado in self._estados
            if estado.esAmbitoEventoSismico() and estado.esRechazado()
        ][0]

        fechaHoraActual: datetime = self.getFechaHora()

        if (
            self._eventoSismicoSeleccionado is not None
            and self._responsable is not None
        ):
            return self._eventoSismicoSeleccionado.rechazar(
                nuevoEstado, self._responsable, fechaHoraActual
            )
        return False

    def buscarUsuario(self) -> Empleado:
        return self._sesion.obtenerUsuario()

    def getFechaHora(self) -> datetime:
        return datetime.now()

    def buscarDetalleEventoSismico(self) -> None:
        if self._eventoSismicoSeleccionado is not None:
            self._datosEventoSismico = (
                self._eventoSismicoSeleccionado.getDatosEventoSismico(self._sismografos)
            )

    def generarSismograma(self) -> None:
        self._sismograma = GestorGenerarSismograma.generarSismograma()

    def tomarSeleccionRevision(self, revision: str, datosEvento: list[str]) -> bool:
        self._tieneDatosValidos = self.validarDatosEventoSismico(revision, datosEvento)
        if self._tieneDatosValidos and revision == "RECHAZAR":
            respuesta: bool = self.rechazarEventoSismico()
            if respuesta:
                return True
            else:
                return False
        else:
            return False
        # Si se quisiera seguir con el flujo, registrando otra accion en otro evento...
        # self.seleccionDatosEventosSismicos()

    # TODO valdiaciones o por lo menos asegurar el formato de recepcion de los datosEvento desde el boundary
    def validarDatosEventoSismico(self, revision: str, datosEvento: list[str]) -> bool:
        condiciones: list[bool] = [
            revision in self._accionesRevision,
            datosEvento[0] != "",  # magnitud
            datosEvento[1] != "",  # alcance
            datosEvento[2] != "",  # origen
        ]
        return all(condiciones)

    def finCasoUso(self) -> None:
        pass
