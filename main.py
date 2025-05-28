import flet as ft

from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision


class Main:

    _boundaryRegistrarRevision: BoundaryRegistrarRevision = BoundaryRegistrarRevision()

    @staticmethod
    def registrarRevisionManual(page):
        pass


ft.app(target=Main.registrarRevisionManual)
