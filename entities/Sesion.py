from datetime import datetime
from entities.Usuario import Usuario


class Sesion:

    def __init__(
        self, fechaHoraDesde: datetime, fechaHoraHasta: datetime, usuario: Usuario
    ) -> None:
        self._fechaHoraDesde: datetime = fechaHoraDesde
        self._fechaHoraHasta: datetime = fechaHoraHasta
        self._usuario: Usuario = usuario

    def obtenerUsuario(self) -> None:
        return self._usuario.getRILogueado()
