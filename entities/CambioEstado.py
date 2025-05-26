from datetime import datetime
from entities.Estado import Estado
from entities.Empleado import Empleado
from entities.MotivoFueraServicio import MotivoFueraServicio

# ahora = datetime.now()                     # 2025-05-25 14:32:10.123456
# ahora.strftime("%d/%m/%Y %H:%M:%S")        # 25/05/2025 14:32:10


class CambioEstado:

    def __init__(
        self,
        estado: Estado,
        responsableInscripcion: Empleado,
        fechaHoraInicio: datetime,
        fechaHoraFin: datetime | None = None,
    ) -> None:
        self._estado: Estado = estado
        self._responsableInscripcion: Empleado = responsableInscripcion
        self._fechaHoraInicio: datetime = fechaHoraInicio
        self._fechaHoraFin: datetime | None = fechaHoraFin
        # No implementamos un metodo para asociar motivos ya que no se requiere para el CU23
        self._motivosFueraServicio: list[MotivoFueraServicio] = []

    # Para utilizar el metodo setter con el decorador "atributo.setter",
    # es necesario tener el metodo getter con el decorador "property"
    @property
    def fechaHoraFin(self) -> datetime | None:
        return self._fechaHoraFin

    @fechaHoraFin.setter
    def fechaHoraFin(self, nuevaFechaHoraFin) -> None:
        self._fechaHoraFin = nuevaFechaHoraFin

    def esEstadoActual(self):
        pass
