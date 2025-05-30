import flet as ft
from datetime import datetime
#from controls.GestorRegistrarRevision import GestorRegistrarRevision


class BoundaryRegistrarRevision:

    def __init__(self) -> None:
        #self._gestorRegistrarRevision: GestorRegistrarRevision = (
        #    GestorRegistrarRevision(self, datetime.now())
        #)
        self._grillaEventosSismicosNoRevisados = None
        self._btnSeleccionarEventoSismicoNoRevisado = None
        self._grillaEventoSismicoSeleccionado = None
        self._btnVisualizarMapa = None
        self._btnModificarDatosEventoSismico = None
        self._campoAccionRevision = None
        #Simulacion de datos
        self._eventosSismicosNoRevisados = [
            {
                "fechaHoraOcurrencia": "2025-05-28 14:30:00",
                "latitudEpicentro": "-31.4201",
                "longitudEpicentro": "-64.1888",
                "latitudHipocentro": "-31.4190",
                "longitudHipocentro": "-64.1895",
                "valorMagnitud": "5.6",
                "clasificacion": "Intermedio",
                "origenGeneracion": "Sismo interplaca",
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
                "origenGeneracion": "Sismo volcánico",
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


    def registrarRevisionManual(self, page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.Colors.WHITE
        page.title = "Red Sísmica"
        page.window_width = 1200
        page.window_height = 700
        page.scroll = "auto"
        page.theme_mode

        self._grillaEventoSismicoSeleccionado = ft.Column(visible=False)
        mapa_container = ft.Container(visible=False)

        def mostrarDatosEventosSismicos(evento):
            
            self._grillaEventoSismicoSeleccionado.controls.clear()
            self._grillaEventoSismicoSeleccionado.controls.append(ft.Text(f"Fecha y hora: {evento['fechaHoraOcurrencia']}", size=14))
            self._grillaEventoSismicoSeleccionado.controls.append(ft.TextField(label="Magnitud", value=evento['valorMagnitud'], width=150))
            self._grillaEventoSismicoSeleccionado.controls.append(ft.Text(f"Ubicación: {evento['latitudHipocentro']}, {evento['longitudHipocentro']}"))
            self._grillaEventoSismicoSeleccionado.controls.append(ft.TextField(label="Origen", value=evento['origenGeneracion'], width=300))
            self._grillaEventoSismicoSeleccionado.controls.append(ft.TextField(label="Alcance", value=evento['alcanceSismico'], width=150))
            self._grillaEventoSismicoSeleccionado.controls.append(ft.Text("Estaciones sísmicas: Estación A, Estación B"))

            self._btnVisualizarMapa = ft.ElevatedButton("Ver mapa", on_click=lambda _: mostrar_mapa())
            self._grillaEventoSismicoSeleccionado.controls.append(self._btnVisualizarMapa)

            self._grillaEventoSismicoSeleccionado.visible = True
            mapa_container.visible = False
            page.update()
        
        def mostrar_mapa():
            mapa_container.content = ft.Image(
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Map_of_the_world_with_outline.svg/1024px-Map_of_the_world_with_outline.svg.png",
                fit=ft.ImageFit.CONTAIN,
                width=300,
                height=300
            )
            mapa_container.visible = True
            page.update()

        self._grillaEventosSismicosNoRevisados = ft.Column([
            ft.Text("Eventos pendientes de revisión", size=18, weight="bold"),
            *[
                ft.Row([
                    ft.Text(e["fechaHoraOcurrencia"], width=150),
                    ft.Text(e["valorMagnitud"], width=50),
                    ft.Text(f'({e["latitudEpicentro"]}, {e["longitudEpicentro"]})', width=150),
                    ft.TextButton("Revisar", on_click=lambda _, ev=e: mostrarDatosEventosSismicos(ev))
                ])
                for e in self._eventosSismicosNoRevisados
            ]
        ])

        grilla_eventos_derivados = ft.Column([
            ft.Text("Eventos derivados a experto", size=18, weight="bold"),
            *[
                ft.Row([
                    ft.Text(e["fechaHoraOcurrencia"], width=150),
                    ft.Text(e["valorMagnitud"], width=50),
                    ft.Text(f'({e["latitudEpicentro"]}, {e["longitudEpicentro"]})', width=150)
                ])
                for e in self._eventosDerivados
            ]
        ])

        self._campoAccionRevision = ft.Dropdown(
            label="Acción final",
            options=[
                ft.dropdown.Option("Rechazar evento"),
                ft.dropdown.Option("Derivar a experto")
            ],
            width=200
        )
        boton_registrar = ft.ElevatedButton("Registrar")

        page.add(
            self._grillaEventosSismicosNoRevisados,
            ft.Row([
                ft.Column([
                    ft.Text("Detalles del evento", size=18, weight="bold"),
                    self._grillaEventoSismicoSeleccionado,
                ],
                expand=2,),
                mapa_container
            ]),
            grilla_eventos_derivados,
            ft.Row([self._campoAccionRevision, boton_registrar], alignment=ft.MainAxisAlignment.END)
        )

    def habilitarVentana(self):
        pass

    def mostrarDatosEventosSismicos(self):
        pass

    def seleccionEventoSismico(self):
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
