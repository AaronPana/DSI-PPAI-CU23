from datetime import datetime
from entities.SerieTemporal import SerieTemporal
from data.estados import estado_data
from data.sismografos import sismografo_data
from data.muestrasSismicas import muestraSismica_data

#Series Temporales de eventoSismico0
SerieTemporal0 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=50,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[0],
)
SerieTemporal0._muestrasSismicas = [muestraSismica_data[0], muestraSismica_data[1], muestraSismica_data[2]]

SerieTemporal1 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 5, 19, 19, 5),
    fechaHoraRegistro=datetime(2025, 5, 19, 19, 5),
    frecuenciaMuestreo=11,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[1],
)
SerieTemporal1._muestrasSismicas = [muestraSismica_data[3], muestraSismica_data[4]]

#Series Temporales de eventoSismico1
SerieTemporal2 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2005, 7, 27, 2, 0),
    fechaHoraRegistro=datetime(2005, 7, 27, 2, 0),
    frecuenciaMuestreo=30,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[2],
)
SerieTemporal2._muestrasSismicas = [muestraSismica_data[5]]

#Series Termporales de eventoSismico2
SerieTemporal3 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 6, 20, 15, 0),
    fechaHoraRegistro=datetime(2025, 6, 20, 15, 0),
    frecuenciaMuestreo=9,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[1],
)
SerieTemporal3._muestrasSismicas = [muestraSismica_data[6], muestraSismica_data[7]]

SerieTemporal4 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 6, 20, 15, 10),
    fechaHoraRegistro=datetime(2025, 6, 20, 15, 0),
    frecuenciaMuestreo=10,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[1],
)
SerieTemporal4._muestrasSismicas = [muestraSismica_data[8]]

SerieTemporal5 = SerieTemporal(
    condicionAlarma=False,
    fechaHoraInicioRegistroMuestras=datetime(2025, 6, 20, 15, 15),
    fechaHoraRegistro=datetime(2025, 6, 20, 15, 0),
    frecuenciaMuestreo=9.5,
    estado=estado_data[11],  # TRANSMITIDA
    sismografo=sismografo_data[1],
)
SerieTemporal5._muestrasSismicas = [muestraSismica_data[9], muestraSismica_data[10]]

serieTemporal_data = [SerieTemporal0, SerieTemporal1, SerieTemporal2, SerieTemporal3, SerieTemporal4, SerieTemporal5]