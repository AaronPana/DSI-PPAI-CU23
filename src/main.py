import flet as ft  # type: ignore

from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision


class Main:
    def __init__(self) -> None:
        self._page: ft.Page | None = None
        self._boundary_registrar: BoundaryRegistrarRevision | None = None
        ft.app(target=self._pantalla_inicial)  # type: ignore

    def _pantalla_inicial(self, page: ft.Page) -> None:
        self._page = page
        self._configurar_pagina()
        self._inicializar_relaciones()
        self._boundary_registrar = BoundaryRegistrarRevision(self._page)

        contenido: ft.Column = self._construir_interfaz()
        self._page.add(contenido)

    def _configurar_pagina(self) -> None:
        """Configura las propiedades iniciales de la página."""
        assert self._page is not None
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.title = "Red Sísmica Argentina"
        self._page.window.maximized = True
        self._page.scroll = ft.ScrollMode.AUTO
        self._page.window.resizable = True
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def _inicializar_relaciones(self) -> None:
        """Inicializa las relaciones entre sismógrafos y series temporales."""
        from data.seriesTemporales import serieTemporal_data
        from data.sismografos import sismografo_data

        sismografo_data[0].seriesTemporales = [serieTemporal_data[0]]
        sismografo_data[1].seriesTemporales = [
            serieTemporal_data[1],
            serieTemporal_data[3],
            serieTemporal_data[4],
            serieTemporal_data[5],
        ]
        sismografo_data[2].seriesTemporales = [serieTemporal_data[2]]

    def _construir_interfaz(self) -> ft.Column:
        """Construye y retorna la interfaz principal."""
        return ft.Column(
            controls=[
                ft.Container(height=30),
                self._crear_logo(),
                self._crear_titulo(),
                ft.Container(height=20),
                self._crear_boton_registro(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )

    def _crear_logo(self) -> ft.Image:
        """Crea el componente del logo."""
        return ft.Image(
            src="src/data/images/logo.png",
            width=80,
            height=80,
            fit=ft.ImageFit.CONTAIN,
        )

    def _crear_titulo(self) -> ft.Text:
        """Crea el componente del título."""
        return ft.Text(
            "Sistema de Monitoreo Sísmico",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_800,
            text_align=ft.TextAlign.CENTER,
        )

    def _crear_boton_registro(self) -> ft.ElevatedButton:
        """Crea el botón de registro de revisión manual."""
        return ft.ElevatedButton(
            text="Registrar revisión manual",
            on_click=self._manejar_registro,
        )

    def _manejar_registro(self, e: ft.ControlEvent) -> None:
        """Maneja el evento de click del botón de registro."""
        assert self._page is not None
        assert self._boundary_registrar is not None
        self._page.controls.clear()  # type: ignore
        self._boundary_registrar.registrarRevisionManual()


if __name__ == "__main__":
    Main()
