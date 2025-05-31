from datetime import datetime
from entities.MuestraSismica import MuestraSismica

# Son de SerieTemporal0
#MuestraSismica1 posee las muestras [DetalleMuestraSismica1, DetalleMuestraSismica1, DetalleMuestraSismica1]
#MuestraSismica2 posee las muestras [DetalleMuestraSismica4, DetalleMuestraSismica5, DetalleMuestraSismica6]
#MuestraSismica3 posee las muestras [DetalleMuestraSismica7, DetalleMuestraSismica8, DetalleMuestraSismica9]
muestraSismica0 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 5)
)

muestraSismica1 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 10),
)

muestraSismica2 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 15)
)

#Son de SerieTemporal1
#muestraSismica3 posee las muestras [DetalleMuestraSismica9, DetalleMuestraSismica10, DetalleMuestraSismica11]
#muestraSismica4 posee las muestras [DetalleMuestraSismica12, DetalleMuestraSismica13, DetalleMuestraSismica14]
muestraSismica3 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 20)
)

muestraSismica4 = MuestraSismica(
    fechaHoraMuestra=datetime(2025, 2, 21, 19, 25),
)

#Son de SerieTemporal2
#muestraSismica6 posee las muestras [DetalleMuestraSismica15, DetalleMuestraSismica16, DetalleMuestraSismica17]
muestraSismica6 = MuestraSismica(
    fechaHoraMuestra=datetime(2005, 7, 27, 2, 0),
)

muestraSismica_data = [muestraSismica0, muestraSismica1, muestraSismica2]
