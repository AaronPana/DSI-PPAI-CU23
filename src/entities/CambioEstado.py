from datetime import datetime
from entities.Estado import Estado
from entities.Empleado import Empleado
from entities.MotivoFueraServicio import MotivoFueraServicio


class CambioEstado:

    def __init__(
        self,
        estado: Estado,
        responsableInscripcion: Empleado,
        fechaHoraInicio: datetime,
    ) -> None:
        self._estado: Estado = estado
        self._responsableInscripcion: Empleado = responsableInscripcion
        self._fechaHoraInicio: datetime = fechaHoraInicio
        self._fechaHoraFin: datetime | None = None
        self._motivosFueraServicio: list[MotivoFueraServicio] = []
        # No implementamos un metodo para asociar motivos ya que no se requiere para el CU23

    # Metodos utilizados en el CU23

    def esEstadoActual(self) -> bool:
        return self._fechaHoraFin is None

    # Métodos de acceso (getters y setters)

    @property
    def estado(self) -> Estado:
        return self._estado

    @estado.setter
    def estado(self, nuevoEstado: Estado) -> None:
        self._estado = nuevoEstado

    @property
    def responsableInscripcion(self) -> Empleado:
        return self._responsableInscripcion

    @responsableInscripcion.setter
    def responsableInscripcion(self, nuevoResponsableInscripcion: Empleado) -> None:
        self._responsableInscripcion = nuevoResponsableInscripcion

    @property
    def fechaHoraInicio(self) -> datetime:
        return self._fechaHoraInicio

    @fechaHoraInicio.setter
    def fechaHoraInicio(self, nuevaFechaHoraInicio: datetime) -> None:
        self._fechaHoraFin = nuevaFechaHoraInicio

    @property
    def fechaHoraFin(self) -> datetime | None:
        return self._fechaHoraFin

    @fechaHoraFin.setter
    def fechaHoraFin(self, nuevaFechaHoraFin: datetime) -> None:
        self._fechaHoraFin = nuevaFechaHoraFin

    @property
    def motivosFueraServicio(self) -> list[MotivoFueraServicio]:
        return self._motivosFueraServicio

    @motivosFueraServicio.setter
    def motivosFueraServicio(
        self, nuevoMotivoFueraServicio: list[MotivoFueraServicio]
    ) -> None:
        self._motivosFueraServicio = nuevoMotivoFueraServicio
