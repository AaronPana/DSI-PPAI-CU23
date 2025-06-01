from datetime import datetime
from entities.SerieTemporal import SerieTemporal
from estados import estado_data
from sismografos import sismografo_data

SerieTemporal0 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=50,
    estado=estado_data[2]._nombreEstado, #AutoDetectado
    sismografo=sismografo_data[0]
)

SerieTemporal1 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=11,
    estado=estado_data[3]._nombreEstado, #pendiente de revision
    sismografo=sismografo_data[1]
)

SerieTemporal2 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2005, 7, 27, 2, 0),
    fechaHoraRegistro=datetime(2005, 7, 27, 2, 0),
    frecuenciaMuestreo=30,
    estado=estado_data[7]._nombreEstado, #confirmado
    sismografo=sismografo_data[2]
)

serieTemporal_data = [SerieTemporal0, SerieTemporal1, SerieTemporal2]

#SerieTemporal0 posee las muestras [MuestraSismica0, MuestraSismica1, MuestraSismica2]
#SerieTemporal1 posee las muestras [MuestraSismica3, MuestraSismica4]
#SerieTemporal2 posee las muestras [MuestraSismica5]

#Tener en cuenta puesto que de esto depende sus fechas y horas!!