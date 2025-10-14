from datetime import datetime
from entities.MuestraSismica import MuestraSismica
from data.detallesMuestrasSismicas import detalleMuestraSismica_data

# Son de SerieTemporal0
muestraSismica0 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 5))
muestraSismica0._detallesMuestraSismica = [
    detalleMuestraSismica_data[0],
    detalleMuestraSismica_data[1],
    detalleMuestraSismica_data[2],
]

muestraSismica1 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 10),)
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
muestraSismica3 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 20))
muestraSismica3._detallesMuestraSismica = [
    detalleMuestraSismica_data[9],
    detalleMuestraSismica_data[10],
    detalleMuestraSismica_data[11],
]

muestraSismica4 = MuestraSismica(fechaHoraMuestra=datetime(2025, 2, 21, 19, 25),)
muestraSismica4._detallesMuestraSismica = [
    detalleMuestraSismica_data[12],
    detalleMuestraSismica_data[13],
    detalleMuestraSismica_data[14],
]

# Son de SerieTemporal2
muestraSismica5 = MuestraSismica(fechaHoraMuestra=datetime(2005, 7, 27, 2, 0))
muestraSismica5._detallesMuestraSismica = [
    detalleMuestraSismica_data[15],
    detalleMuestraSismica_data[16],
    detalleMuestraSismica_data[17],
]

# Son de SerieTemporal3
muestraSismica6 = MuestraSismica(fechaHoraMuestra=datetime(2025, 6, 20, 15, 0))
muestraSismica6._detallesMuestraSismica = [
    detalleMuestraSismica_data[18],
    detalleMuestraSismica_data[19],
    detalleMuestraSismica_data[20],
]
muestraSismica7 = MuestraSismica(fechaHoraMuestra=datetime(2025, 6, 20, 15, 5))
muestraSismica7._detallesMuestraSismica = [
    detalleMuestraSismica_data[21],
    detalleMuestraSismica_data[22],
    detalleMuestraSismica_data[23],
]

# Son de SerieTemporal4
muestraSismica8 = MuestraSismica(fechaHoraMuestra=datetime(2025, 6, 20, 15, 10))
muestraSismica8._detallesMuestraSismica = [
    detalleMuestraSismica_data[24],
    detalleMuestraSismica_data[25],
    detalleMuestraSismica_data[26],
]

## Son de SerieTemporal5
muestraSismica9 = MuestraSismica(fechaHoraMuestra=datetime(2025, 6, 20, 15, 15))
muestraSismica9._detallesMuestraSismica = [
    detalleMuestraSismica_data[27],
    detalleMuestraSismica_data[28],
    detalleMuestraSismica_data[29],
]
muestraSismica10 = MuestraSismica(fechaHoraMuestra=datetime(2025, 6, 20, 15, 20))
muestraSismica10._detallesMuestraSismica = [
    detalleMuestraSismica_data[30],
    detalleMuestraSismica_data[31],
    detalleMuestraSismica_data[32],
]

muestraSismica_data = [
    muestraSismica0,
    muestraSismica1,
    muestraSismica2,
    muestraSismica3,
    muestraSismica4,
    muestraSismica5,
    muestraSismica6,
    muestraSismica7,
    muestraSismica8,
    muestraSismica9,
    muestraSismica10,
]
