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
        self._fechaHoraHasta: datetime | None = fechaHoraHasta
        self._usuario: Usuario = usuario

    # Metodos utilizados en el CU23

    def obtenerUsuario(self) -> Empleado:
        return self._usuario.getRILogueado()

    # Métodos de acceso (getters y setters)

    @property
    def fechaHoraDesde(self) -> datetime:
        return self._fechaHoraDesde

    @fechaHoraDesde.setter
    def fechaHoraDesde(self, nuevaFechaHoraDesde: datetime) -> None:
        self._fechaHoraDesde = nuevaFechaHoraDesde

    @property
    def fechaHoraHasta(self) -> datetime | None:
        return self._fechaHoraHasta

    @fechaHoraHasta.setter
    def fechaHoraHasta(self, nuevaFechaHoraHasta: datetime) -> None:
        self._fechaHoraHasta = nuevaFechaHoraHasta

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @usuario.setter
    def usuario(self, nuevoUsuario: Usuario) -> None:
        self._usuario = nuevoUsuario
