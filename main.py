import flet as ft
from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision


class Main:
    def __init__(self):
        ft.app(target=self.pantalla_inicial)

    def pantalla_inicial(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.title = "Red Sísmica"
        self.page.window_maximized = True
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window_resizable = True
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.inicializar_relaciones()

        self.boundary_registrar = BoundaryRegistrarRevision(self.page)
        boton = ft.ElevatedButton(
            text="Registrar revisión manual",
            on_click=lambda e: [
                self.page.controls.clear(),
                self.boundary_registrar.registrarRevisionManual(),
            ],
        )

        self.page.add(
            ft.Column(
                [
                    ft.Text(
                        "Sistema de Monitoreo Sísmico",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    boton,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def inicializar_relaciones(self):
        from data.seriesTemporales import serieTemporal_data
        from data.sismografos import sismografo_data

        serieTemporal_data[0].sismografo = sismografo_data[0]
        serieTemporal_data[1].sismografo = sismografo_data[1]
        serieTemporal_data[2].sismografo = sismografo_data[2]
        serieTemporal_data[3].sismografo = sismografo_data[1]
        serieTemporal_data[4].sismografo = sismografo_data[1]
        serieTemporal_data[5].sismografo = sismografo_data[1]

        sismografo_data[0]._seriesTemporales = [serieTemporal_data[0]]
        sismografo_data[1]._seriesTemporales = [
            serieTemporal_data[1],
            serieTemporal_data[3],
            serieTemporal_data[4],
            serieTemporal_data[5],
        ]
        sismografo_data[2]._seriesTemporales = [serieTemporal_data[2]]


Main()
