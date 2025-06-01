from datetime import date, datetime
from entities.CambioEstado import CambioEstado
from entities.ModeloSismografo import ModeloSismografo
from entities.Sismografo import Sismografo
from data.estacionesSismologicas import estacionSismologica_data
from data.estados import estado_data
from data.seriesTemporales import serieTemporal_data
from data.empleados import Empleado0

Sismografo0 = Sismografo(
    fechaAdquisicion=date(2004, 4, 3),
    identificadorSismografo="1",
    nroSerie=4401,
    estacionSismologica=estacionSismologica_data[0],
    estadoActual=estado_data[0],
    modeloSismografo=ModeloSismografo(),
)

Sismografo0._cambiosEstado.append(
    CambioEstado(estado_data[0], Empleado0, datetime.now())
)

Sismografo0._seriesTemporales = [serieTemporal_data[0]]

Sismografo1 = Sismografo(
    fechaAdquisicion=date(2007, 6, 2),
    identificadorSismografo="2",
    nroSerie=4402,
    estacionSismologica=estacionSismologica_data[1],
    estadoActual=estado_data[0],
    modeloSismografo=ModeloSismografo(),
)

Sismografo1._cambiosEstado.append(
    CambioEstado(estado_data[0], Empleado0, datetime.now())
)

Sismografo1._seriesTemporales = [serieTemporal_data[1]]

Sismografo2 = Sismografo(
    fechaAdquisicion=date(2009, 12, 2),
    identificadorSismografo="3",
    nroSerie=4403,
    estacionSismologica=estacionSismologica_data[2],
    estadoActual=estado_data[0],
    modeloSismografo=ModeloSismografo(),
)

Sismografo2._cambiosEstado.append(
    CambioEstado(estado_data[0], Empleado0, datetime.now())
)

Sismografo2._seriesTemporales = [serieTemporal_data[2]]

sismografo_data = [Sismografo0, Sismografo1, Sismografo2]
# El sismografo n pertenece a la estacion sismologica n
