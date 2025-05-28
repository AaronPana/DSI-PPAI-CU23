from datetime import datetime
from entities.Empleado import Empleado
from entities.Usuario import Usuario


class Sesion:

    def __init__(
        self,
        fechaHoraDesde: datetime,
        fechaHoraHasta: datetime | None,
        usuario: Usuario,
    ) -> None:
        self._fechaHoraDesde: datetime = fechaHoraDesde
        # Se deberia hacer un setter para aasginar fechHoraHasta
        # pero no se utiliza en el CU23
        self._fechaHoraHasta: datetime | None = fechaHoraHasta
        self._usuario: Usuario = usuario

    def obtenerUsuario(self) -> Empleado:
        return self._usuario.getRILogueado()
