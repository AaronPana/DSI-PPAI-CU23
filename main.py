import flet as ft

from boundaries.BoundaryRegistrarRevision import BoundaryRegistrarRevision


class Main:

    def __init__(self):
        ft.app(target=Main.registrarRevisionManual)

    @staticmethod
    def registrarRevisionManual(page):
        boundaryRegistrarRevision: BoundaryRegistrarRevision = BoundaryRegistrarRevision(page)
        boundaryRegistrarRevision.registrarRevisionManual()

Main()