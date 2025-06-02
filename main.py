import flet as ft
from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision

class Main:
    def __init__(self):
        ft.app(target=self.pantalla_inicial)

    def pantalla_inicial(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.title = "Red Sísmica"
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window_width = 700
        self.page.window_height = 250
        self.page.window_resizable = False

        self.boundary_registrar = BoundaryRegistrarRevision(self.page)

        boton = ft.ElevatedButton(
            text="Registrar revisión manual",
            on_click=self.boundary_registrar.registrarRevisionManual 
        )

        self.page.add(
            ft.Column([
                ft.Text("Sistema de Monitoreo Sísmico", size=20, weight="bold"),
                boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

Main()
