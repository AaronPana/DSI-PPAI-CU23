from datetime import datetime
from entities.CambioEstado import CambioEstado
from data.empleados import empleado_data
from data.estados import estado_data

CambioEstado0 = CambioEstado(
    estado=estado_data[2],
    responsableInscripcion=empleado_data[0],
    fechaHoraInicio=datetime(2025, 5, 19, 19, 5),
    fechaHoraFin=None
)

CambioEstado1 = CambioEstado(
    estado=estado_data[7],
    responsableInscripcion=empleado_data[0],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 0),
    fechaHoraFin=datetime(2005, 7, 28, 2, 0),
)

cambioEstado_data = [CambioEstado0, CambioEstado1]