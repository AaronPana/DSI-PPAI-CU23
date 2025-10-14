from datetime import datetime
from entities.CambioEstado import CambioEstado
from data.empleados import empleado_data
from data.estados import estado_data

CambioEstado0 = CambioEstado(
    estado=estado_data[2], #AUTODETECTADO
    responsableInscripcion=empleado_data[1],
    fechaHoraInicio=datetime(2025, 5, 19, 19, 5),
)

CambioEstado1 = CambioEstado(
    estado=estado_data[2], #AUTODETECTADO
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 0),
)
CambioEstado1.fechaHoraFin = datetime(2005, 7, 27, 2, 5)

CambioEstado2 = CambioEstado(
    estado=estado_data[5], #EN_REVISION
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 5),
)
CambioEstado2.fechaHoraFin = datetime(2005, 7, 27, 2, 10)

CambioEstado3 = CambioEstado(
    estado=estado_data[7], #CONFIRMADO
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2005, 7, 27, 2, 10),
)

CambioEstado4 = CambioEstado(
    estado=estado_data[2], #AUTODETECTADO
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2025, 6, 20, 15, 0)
)
CambioEstado4.fechaHoraFin = datetime(2025, 6, 20, 15, 5)

CambioEstado5 = CambioEstado(
    estado=estado_data[3], #PENDIENTE_REVISION
    responsableInscripcion=empleado_data[2],
    fechaHoraInicio=datetime(2025, 6, 20, 15, 5)
)

cambioEstado_data = [CambioEstado0, CambioEstado1, CambioEstado2, CambioEstado3, CambioEstado4, CambioEstado5]
