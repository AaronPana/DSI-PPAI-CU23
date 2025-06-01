from datetime import datetime
from entities.CambioEstado import CambioEstado
from data.empleados import empleado_data
from data.estados import estado_data

CambioEstado0 = CambioEstado(
    estado=estado_data[2],
    responsableInscripcion=empleado_data[1],
    fechaHoraInicio=datetime(2025, 5, 19, 19, 5),
)

CambioEstado1 = CambioEstado(
    estado=estado_data[7],
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 0),
)

CambioEstado2 = CambioEstado(
    estado=estado_data[5],
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 0),
)

CambioEstado2.fechaHoraFin = datetime(2005, 7, 28, 2, 0)

cambioEstado_data = [CambioEstado0, CambioEstado1, CambioEstado2]
