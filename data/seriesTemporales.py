from datetime import datetime
from entities.SerieTemporal import SerieTemporal
from data.estados import estado_data
from data.sismografos import sismografo_data
from data.muestrasSismicas import muestraSismica_data

SerieTemporal0 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=50,
    estado=estado_data[2],  # AutoDetectado
    sismografo=sismografo_data[0],
)

SerieTemporal0._muestrasSismicas = [
    muestraSismica_data[0],
    muestraSismica_data[1],
    muestraSismica_data[2],
]

SerieTemporal1 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=11,
    estado=estado_data[3],  # pendiente de revision
    sismografo=sismografo_data[1],
)

SerieTemporal1._muestrasSismicas = [muestraSismica_data[3], muestraSismica_data[4]]

SerieTemporal2 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2005, 7, 27, 2, 0),
    fechaHoraRegistro=datetime(2005, 7, 27, 2, 0),
    frecuenciaMuestreo=30,
    estado=estado_data[7],  # confirmado
    sismografo=sismografo_data[2],
)

SerieTemporal2._muestrasSismicas = [muestraSismica_data[5]]

serieTemporal_data = [SerieTemporal0, SerieTemporal1, SerieTemporal2]

# SerieTemporal0 posee las muestras [MuestraSismica0, MuestraSismica1, MuestraSismica2]
# SerieTemporal1 posee las muestras [MuestraSismica3, MuestraSismica4]
# SerieTemporal2 posee las muestras [MuestraSismica5]

# Tener en cuenta puesto que de esto depende sus fechas y horas!!
