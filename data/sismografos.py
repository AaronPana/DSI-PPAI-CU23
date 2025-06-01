from datetime import date
from entities.Sismografo import Sismografo
from estados import estado_data

Sismografo0 = Sismografo(
    fechaAdquisicion=date(2004, 4, 3),
    identificadorSismografo=1,
    nroSerie=4401,
    estadoActual=estado_data[10],
    modeloSismografo="-"
)

Sismografo1 = Sismografo(
    fechaAdquisicion=date(2007, 6, 2),
    identificadorSismografo=2,
    nroSerie=4402,
    estadoActual=estado_data[10],
    modeloSismografo="-"
)

Sismografo2 = Sismografo(
    fechaAdquisicion=date(2009, 12, 2),
    identificadorSismografo=3,
    nroSerie=4403,
    estadoActual=estado_data[10],
    modeloSismografo="-"
)

sismografo_data = [Sismografo0, Sismografo1, Sismografo2]
#El sismografo n pertenece a la estacion sismologica n