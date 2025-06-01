import flet as ft


class BoundaryRegistrarRevision:

    def __init__(self, page: ft.Page) -> None:
        self._page: ft.Page = page
        #self._gestorRegistrarRevision: GestorRegistrarRevision = (
        #    GestorRegistrarRevision(self, datetime.now())
        #)
        self._grillaEventosSismicosNoRevisados: ft.DataTable = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Fecha y Hora de Ocurrencia")),
                ft.DataColumn(label=ft.Text("Latitud Epicentro")),
                ft.DataColumn(label=ft.Text("Longitud Epicentro")),
                ft.DataColumn(label=ft.Text("Latitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Longitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Magnitud")),
                ft.DataColumn(label=ft.Text("Clasificación")),
                ft.DataColumn(label=ft.Text("Origen Generación")),
                ft.DataColumn(label=ft.Text("Alcance Sísmico")),
            ],
            rows=[],
            heading_row_color=ft.colors.BLUE_800,
            data_row_color={ft.MaterialState.SELECTED: ft.colors.with_opacity(0.3, ft.colors.GREY_500)}
        )
        self._btnSeleccionarEventoSismicoNoRevisado = None
        self._grillaEventoSismicoSeleccionado = None
        self._btnVisualizarMapa = None
        self._btnModificarDatosEventoSismico = None
        self._campoAccionRevision = None
        # Simulacion de datos
        self._eventosSismicosNoRevisados = [
            {
                "fechaHoraOcurrencia": "2025-05-28 14:30:00",
                "latitudEpicentro": "-31.4201",
                "longitudEpicentro": "-64.1888",
                "latitudHipocentro": "-31.4190",
                "longitudHipocentro": "-64.1895",
                "valorMagnitud": "5.6",
                "clasificacion": "Intermedio",
                "origenDeGeneracion": "Sismo interplaca",
                "alcanceSismico": "Regional"
            },
            {
                "fechaHoraOcurrencia": "2025-05-27 03:45:12",
                "latitudEpicentro": "-32.0123",
                "longitudEpicentro": "-63.1234",
                "latitudHipocentro": "-32.0101",
                "longitudHipocentro": "-63.1256",
                "valorMagnitud": "3.9",
                "clasificacion": "Superficial",
                "origenDeGeneracion": "Sismo volcánico",
                "alcanceSismico": "Local"
            }
        ]

        self._eventosDerivados = [
            {
                "fechaHoraOcurrencia": "2025-05-23 17:45:00",
                "latitudEpicentro": "-32.5000",
                "longitudEpicentro": "-71.6000",
                "valorMagnitud": "5.0"
            },
            {
                "fechaHoraOcurrencia": "2025-05-22 10:20:00",
                "latitudEpicentro": "-30.2000",
                "longitudEpicentro": "-70.9000",
                "valorMagnitud": "4.3"
            }
        ]

    def registrarRevisionManual(self):
        self._page.title = "Red Sísmica"
        self._page.window_maximized = True
        self._page.scroll = ft.ScrollMode.AUTO

        self.cargarEventosSismicos(self._eventosSismicosNoRevisados)

        self._page.add(self._grillaEventosSismicosNoRevisados)

    def habilitarVentana(self):
        pass

    # TODO cambiar datos de celdas por "objeto.atributo"
    def cargarEventosSismicos(self, eventos):
        filas: list[ft.DataRow] = []
        for index, evento in enumerate(eventos):
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(evento["fechaHoraOcurrencia"]))),
                    ft.DataCell(ft.Text(str(evento["latitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["latitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["valorMagnitud"]))),
                    ft.DataCell(ft.Text(str(evento["clasificacion"]))),
                    ft.DataCell(ft.Text(str(evento["origenDeGeneracion"]))),
                    ft.DataCell(ft.Text(str(evento["alcanceSismico"]))),
                ],
                selected=False,
                on_select_changed=lambda selected, i=index: self._onSelectRow(i, selected)
            )
            filas.append(fila)

        self._grillaEventosSismicosNoRevisados.rows = filas
    
    def _onSelectRow(self, index, selected):
        if selected:
            for i, row in enumerate(self._grillaEventosSismicosNoRevisados.rows):
                row.selected = (i == index)
            evento = self._eventosSismicosNoRevisados[index]
            print(f"Evento seleccionado: {evento}")
            self._page.update()

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
