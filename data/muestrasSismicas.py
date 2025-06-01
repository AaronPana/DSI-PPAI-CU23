from datetime import datetime
from entities.MuestraSismica import MuestraSismica
from data.detallesMuestrasSismicas import detalleMuestraSismica_data

# Son de SerieTemporal0
# MuestraSismica0 posee las muestras [DetalleMuestraSismica1, DetalleMuestraSismica2, DetalleMuestraSismica3]
# MuestraSismica1 posee las muestras [DetalleMuestraSismica4, DetalleMuestraSismica5, DetalleMuestraSismica6]
# MuestraSismica2 posee las muestras [DetalleMuestraSismica7, DetalleMuestraSismica8, DetalleMuestraSismica9]
muestraSismica0 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 5))
muestraSismica0._detallesMuestraSismica = [
    detalleMuestraSismica_data[0],
    detalleMuestraSismica_data[1],
    detalleMuestraSismica_data[2],
]

muestraSismica1 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 10),
)
muestraSismica1._detallesMuestraSismica = [
    detalleMuestraSismica_data[3],
    detalleMuestraSismica_data[4],
    detalleMuestraSismica_data[5],
]

muestraSismica2 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 15))
muestraSismica2._detallesMuestraSismica = [
    detalleMuestraSismica_data[6],
    detalleMuestraSismica_data[7],
    detalleMuestraSismica_data[8],
]

# Son de SerieTemporal1
# muestraSismica3 posee las muestras [DetalleMuestraSismica9, DetalleMuestraSismica10, DetalleMuestraSismica11]
# muestraSismica4 posee las muestras [DetalleMuestraSismica12, DetalleMuestraSismica13, DetalleMuestraSismica14]
muestraSismica3 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 20))
muestraSismica3._detallesMuestraSismica = [
    detalleMuestraSismica_data[9],
    detalleMuestraSismica_data[10],
    detalleMuestraSismica_data[11],
]

muestraSismica4 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 25),
)
muestraSismica4._detallesMuestraSismica = [
    detalleMuestraSismica_data[12],
    detalleMuestraSismica_data[13],
    detalleMuestraSismica_data[14],
]

# Son de SerieTemporal2
# muestraSismica5 posee las muestras [DetalleMuestraSismica15, DetalleMuestraSismica16, DetalleMuestraSismica17]
muestraSismica5 = MuestraSismica(
    fechaHoraMuestra=datetime(2005, 7, 27, 2, 0),
)
muestraSismica5._detallesMuestraSismica = [
    detalleMuestraSismica_data[15],
    detalleMuestraSismica_data[16],
    detalleMuestraSismica_data[17],
]

muestraSismica_data = [
    muestraSismica0,
    muestraSismica1,
    muestraSismica2,
    muestraSismica3,
    muestraSismica4,
    muestraSismica5,
]
