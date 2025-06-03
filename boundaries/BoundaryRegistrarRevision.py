import flet as ft
from datetime import datetime


class BoundaryRegistrarRevision:
    def __init__(self, page: ft.Page) -> None:
        from controls.GestorRegistrarRevision import GestorRegistrarRevision
        self._gestorRegistrarRevision: GestorRegistrarRevision = (GestorRegistrarRevision(self, datetime.now()))
        self._page: ft.Page = page

        # ATRIBUTOS
        self.campos_evento = {}
        self.nombres_campos = ["Fecha", "Hora", "Latitud", "Longitud", "Magnitud"]
        for campo in self.nombres_campos:
            self.campos_evento[campo] = ft.TextField(
                label=campo, disabled=True, expand=True
            )

        self._btnModificar = ft.ElevatedButton("Modificar", on_click=self.modificarEvento)
        self._btnGuardar = ft.ElevatedButton("Guardar Evento Sismico", on_click=lambda e: self.guardarCambiosEvento)
        self._btnCancelar = ft.ElevatedButton("Cancelar Modificacion", on_click=lambda e: self.cancelarCambiosEvento)
        self._btnCancelarCU = ft.ElevatedButton("Cancelar", on_click=lambda e: self.cancelarCasoUso)
        self._btnVisualizarMapa = ft.ElevatedButton("Ver mapa", on_click=lambda e: self.mostrarMapa)
        self._btnRegistrarAccion = ft.ElevatedButton(text="Registrar", on_click=lambda e: self.tomarSeleccionRevision(self.campos_evento))

        self._dropdownAccionRevision = ft.Dropdown(
            label="Acción de revisión",
            options=[
                ft.dropdown.Option("CONFIRMAR"),
                ft.dropdown.Option("RECHAZAR"),
                ft.dropdown.Option("SOLICITAR REVISION"),
            ],
            width=300,
        )

        self.imagen_sismograma = ft.Image(
            key="mapaSismograma",
            src="../data/sismograma.png",
            visible=False, width=400, height=250, fit=ft.ImageFit.CONTAIN)

        self.contenedor_sismograma = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Sismograma",
                        size=16,
                        weight="bold",
                        color=ft.Colors.BLUE_800,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(
                        content=self.imagen_sismograma,
                        alignment=ft.alignment.center,
                        expand=True,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            width=420,
            height=300,
            bgcolor=ft.Colors.GREY_100,
            border_radius=10,
            padding=15,
            alignment=ft.alignment.center,
            visible=False,
        )

        self.formulario_edicion = ft.Column(
            [
                ft.Text(
                    "Detalles del evento sísmico seleccionado", size=20, weight="bold"
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                *[
                                    self.campos_evento[campo]
                                    for campo in self.nombres_campos
                                ]
                            ],
                            expand=1,
                        )
                    ]
                ),
            ],
            visible=False,
        )

        self._eventosSismicosNoRevisados = []
        self._grillaEventosSismicosNoRevisados = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Fecha y Hora")),
                ft.DataColumn(label=ft.Text("Lat. Epicentro")),
                ft.DataColumn(label=ft.Text("Long. Epicentro")),
                ft.DataColumn(label=ft.Text("Lat. Hipocentro")),
                ft.DataColumn(label=ft.Text("Long. Hipocentro")),
                ft.DataColumn(label=ft.Text("Magnitud")),
            ],
            rows=[],
            heading_row_color=ft.Colors.BLUE_800,
            expand=True,
        )

        self._grillaEventoSismicoSeleccionado = ft.Container(
            content=ft.ListView(
                controls=[], expand=True, spacing=10, auto_scroll=False
            ),
            visible=False,
            width=950,
            height=280,
            bgcolor=ft.Colors.GREY_100,
            border_radius=10,
            padding=10,
        )

        self.barra_superior = ft.Row(
            controls=[self._btnCancelarCU], alignment=ft.MainAxisAlignment.END
        )

        self.barra_edicion = ft.Row(
            controls=[self._btnModificar, self._btnGuardar, self._btnCancelar],
            visible=False,
            spacing=10,
        )

        self.barra_acciones = ft.Row(
            controls=[
                self._dropdownAccionRevision,
                self._btnRegistrarAccion,
                self._btnVisualizarMapa,
            ],
            visible=False,
            spacing=10,
        )

        self.contenedor_principal = ft.Column(
            controls=[
                self.barra_superior,
                ft.Text("Eventos Sísmicos No Revisados", size=18, weight="bold"),
                ft.Container(self._grillaEventosSismicosNoRevisados, height=200),
                ft.Divider(),
                ft.Text("Detalle del Evento Seleccionado", size=18, weight="bold"),
                self._grillaEventoSismicoSeleccionado,
                ft.Row(
                    [
                        self.contenedor_sismograma,
                        ft.Column(
                            [self.formulario_edicion, self.barra_edicion], expand=True
                        ),
                    ],
                    spacing=20,
                ),
                self.barra_acciones,
            ],
            spacing=15,
            expand=True,
        )

    # METODOS DE BOUNDARY

    def registrarRevisionManual(self, evento):
        self.habilitarVentana(evento)

    def habilitarVentana(self, e):
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.title = "Red Sísmica"
        self._page.scroll = ft.ScrollMode.AUTO
        self._page.window_width = 1200
        self._page.window_height = 750
        self._page.window_resizable = True
        self._page.padding = 20
        self._page.add(self.contenedor_principal)
        self._gestorRegistrarRevision.seleccionDatosEventosSismicos()

    def mostrarDatosEventosSismicos(self, datos_eventos):
        self._eventosSismicosNoRevisados = datos_eventos
        if self._eventosSismicosNoRevisados:
            filas: list[ft.DataRow] = []
            for index, evento in enumerate(datos_eventos):
                fila = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(evento["fechaHoraOcurrencia"]))),
                        ft.DataCell(ft.Text(str(evento["latitudEpicentro"]))),
                        ft.DataCell(ft.Text(str(evento["longitudEpicentro"]))),
                        ft.DataCell(ft.Text(str(evento["latitudHipocentro"]))),
                        ft.DataCell(ft.Text(str(evento["longitudHipocentro"]))),
                        ft.DataCell(ft.Text(str(evento["valorMagnitud"]))),
                    ],
                    selected=False,
                    on_select_changed=lambda selected,
                    i=index: self.seleccionEventoSismico(i, selected),
                )
                filas.append(fila)
            self._grillaEventosSismicosNoRevisados.rows = filas
            self._grillaEventosSismicosNoRevisados.visible = True
            if hasattr(self, "_mensajeSinEventos"):
                self._page.controls.remove(self._mensajeSinEventos)
        else:
            self._grillaEventosSismicosNoRevisados.rows = []
            self._grillaEventosSismicosNoRevisados.visible = False
            self._mensajeSinEventos = ft.Text(
                "No hay sismos auto detectados que aún no han sido revisados.",
                size=18,
                color=ft.Colors.RED_700,
                weight="bold",
            )
            self._page.controls.append(self._mensajeSinEventos)

        self._page.update()

    def seleccionEventoSismico(self, index, selected):
        if selected:
            for i, row in enumerate(self._grillaEventosSismicosNoRevisados.rows):
                row.selected = i == index
            evento_dict = self._eventosSismicosNoRevisados[index]

            fecha_hora = evento_dict["fechaHoraOcurrencia"].split()
            self.campos_evento["Fecha"].value = (
                fecha_hora[0] if len(fecha_hora) > 0 else ""
            )
            self.campos_evento["Hora"].value = (
                fecha_hora[1] if len(fecha_hora) > 1 else ""
            )
            self.campos_evento["Latitud"].value = str(evento_dict["latitudEpicentro"])
            self.campos_evento["Longitud"].value = str(evento_dict["longitudEpicentro"])
            self.campos_evento["Magnitud"].value = str(evento_dict["valorMagnitud"])

            self.evento_original = {
                "Fecha": self.campos_evento["Fecha"].value,
                "Hora": self.campos_evento["Hora"].value,
                "Latitud": self.campos_evento["Latitud"].value,
                "Longitud": self.campos_evento["Longitud"].value,
                "Magnitud": self.campos_evento["Magnitud"].value,
            }

            self._gestorRegistrarRevision.seleccionEventoSismico(evento_dict)
            self._page.update()

    def mostrarDatosEventoSismico(self, evento_extendido):
        secciones_estaciones = []
        for estacion in evento_extendido["infoSeriesTemporales"]:
            muestras = []
            for muestra in estacion["datosMuestras"]:
                detalles = "\n".join(
                    f"{d['denominacion']}: {d['valor']} {d['nombreUnidadMedida']}"
                    for d in muestra["datosDetalles"]
                )
                muestras.append(
                    ft.Container(
                        content=ft.Text(
                            f"Muestra: {muestra['fechaHoraMuestra']}\n{detalles}"
                        ),
                        bgcolor=ft.Colors.BLUE_50,
                        padding=8,
                        border_radius=8,
                    )
                )
            secciones_estaciones.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                f"Estación: {estacion['estacionSismologica']}",
                                weight="bold",
                            ),
                            ft.Text(f"Fecha Registro: {estacion['fechaHoraRegistro']}"),
                            ft.Text(
                                f"Frecuencia de Muestreo: {estacion['frecuenciaMuestreo']} Hz"
                            ),
                            ft.Text(f"Alarma: {estacion['condicionAlarma']}"),
                            ft.Divider(),
                            *muestras,
                        ],
                        spacing=8,
                    ),
                    bgcolor=ft.Colors.GREY_200,
                    padding=10,
                    border_radius=10,
                )
            )
        self._grillaEventoSismicoSeleccionado.content.controls = [
            ft.Text("Información Extendida del Evento", size=18, weight="bold"),
            ft.Text(f"Alcance Sísmico: {evento_extendido['alcanceSismico']}"),
            ft.Text(f"Origen de Generación: {evento_extendido['origenGeneracion']}"),
            ft.Text(f"Clasificación: {evento_extendido['clasificacion']}"),
            ft.Divider(),
            *secciones_estaciones,
        ]
        self._grillaEventoSismicoSeleccionado.visible = True
        self._page.update()
        self.habilitarOpcionVisualizarMapa(True)
        self._page.update()

    def mostrarSismograma(self, e=None, src=None):
        if src:
            self.imagen_sismograma.src = src
        self.imagen_sismograma.visible = True
        self.contenedor_sismograma.visible = True

    def habilitarOpcionVisualizarMapa(self, bool):
        self.barra_acciones.visible = bool
        self._page.update()

    def mostrarMapa(self):
        pass

    def habilitarModificarDatosEventoSismico(self, habilitar: bool):
        self.barra_edicion.visible = habilitar
        self._page.update()

    def modificarEvento(self, e):
        self.formulario_edicion.visible = True
        for campo in self.nombres_campos:
            self.campos_evento[campo].disabled = False
        self.barra_edicion.visible = True
        index_seleccionado = next(
            (
                i
                for i, row in enumerate(self._grillaEventosSismicosNoRevisados.rows)
                if row.selected
            ),
            None,
        )
        if index_seleccionado is not None:
            evento = self._eventosSismicosNoRevisados[index_seleccionado]
            self.evento_original = {
                "Fecha": evento["fechaHoraOcurrencia"].split()[0],
                "Hora": evento["fechaHoraOcurrencia"].split()[1],
                "Latitud": evento["latitudEpicentro"],
                "Longitud": evento["longitudEpicentro"],
                "Magnitud": evento["valorMagnitud"],
            }

            for campo, valor in self.evento_original.items():
                self.campos_evento[campo].value = valor

        self._page.update()

    def guardarCambiosEvento(self, e):
        index_seleccionado = next(
            (
                i
                for i, row in enumerate(self._grillaEventosSismicosNoRevisados.rows)
                if row.selected
            ),
            None,
        )

        if index_seleccionado is None:
            return

        datos_actualizados = {
            campo: self.campos_evento[campo].value for campo in self.nombres_campos
        }

        evento = self._eventosSismicosNoRevisados[index_seleccionado]
        evento["fechaHoraOcurrencia"] = (
            f"{datos_actualizados['Fecha']} {datos_actualizados['Hora']}"
        )
        evento["latitudEpicentro"] = datos_actualizados["Latitud"]
        evento["longitudEpicentro"] = datos_actualizados["Longitud"]
        evento["valorMagnitud"] = datos_actualizados["Magnitud"]

        fila = self._grillaEventosSismicosNoRevisados.rows[index_seleccionado]
        fila.cells[0].content.value = evento["fechaHoraOcurrencia"]
        fila.cells[1].content.value = evento["latitudEpicentro"]
        fila.cells[2].content.value = evento["longitudEpicentro"]
        fila.cells[5].content.value = evento["valorMagnitud"]

        for campo in self.nombres_campos:
            self.campos_evento[campo].disabled = True

        self.barra_edicion.visible = False
        self._page.update()

    def cancelarCambiosEvento(self, e):
        if hasattr(self, "evento_original"):
            for campo, valor in self.evento_original.items():
                self.campos_evento[campo].value = valor

        for campo in self.nombres_campos:
            self.campos_evento[campo].disabled = True

        self.barra_edicion.visible = False
        self._page.update()

    def solicitarAccionRevision(self):
        self.barra_acciones.visible = True
        self._page.update()

    def tomarSeleccionRevision(self):
        accion = self._dropdownAccionRevision.value
        datos_evento = [campo.value for campo in self.campos_evento.values()]
        accion_mapeada = {
            "CONFIRMAR": "CONFIRMAR",
            "RECHAZAR": "RECHAZAR",
            "SOLICITAR REVISION": "SOLICITAR_REVISION",
        }.get(accion, "")
        if accion_mapeada:
            print(accion_mapeada, datos_evento)
            resultado = self._gestorRegistrarRevision.tomarSeleccionRevision(
                accion_mapeada, datos_evento
            )
            if resultado:
                dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("✅ Éxito"),
                    content=ft.Text("La accion fue registrada con éxito"),
                    actions=[
                        ft.TextButton("Aceptar", on_click=lambda e: self._page.close(dlg))
                    ],
                )
                self._page.open(dlg)

    def finCasoUso(self, e):
        pass