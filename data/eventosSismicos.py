from datetime import datetime
from entities.EventoSismico import EventoSismico
from entities.MagnitudRichter import MagnitudRichter
from data.estados import estado_data
from data.empleados import empleado_data
from data.clasificacionesSismos import clasificacionSismo_data
from data.alcancesSismos import alcanceSismo_data
from data.cambiosEstados import cambioEstado_data
from data.origenDeGeneracion import origenDeGeneracion_data
from data.seriesTemporales import serieTemporal_data

eventoSismico0 = EventoSismico(
    fechaHoraOcurrencia=datetime(2025, 5, 19, 19, 5),
    fechaHoraFin=datetime(2025, 5, 19, 19, 40),
    latitudEpicentro=-34.6037,
    longitudEpicentro=-58.3816,
    latitudHipocentro=-34.6037,
    longitudHipocentro=-58.3816,
    valorMagnitud=4.5,
    clasificacionSisimo=clasificacionSismo_data[1],
    magnitud=MagnitudRichter(),
    origenDeGeneracion=origenDeGeneracion_data[0],
    alcanceSismo=alcanceSismo_data[0],
    estadoActual=estado_data[2],
    analistaSupervisor=empleado_data[2],
)

eventoSismico0._cambiosEstado = [cambioEstado_data[2], cambioEstado_data[1]]

eventoSismico0._seriesTemporales = [serieTemporal_data[0], serieTemporal_data[1]]

eventoSismico1 = EventoSismico(
    fechaHoraOcurrencia=datetime(2005, 7, 27, 2, 0),
    fechaHoraFin=datetime(2005, 7, 28, 2, 0),
    latitudEpicentro=-34.6037,
    longitudEpicentro=-58.3816,
    latitudHipocentro=-34.6040,
    longitudHipocentro=-58.3810,
    valorMagnitud=5.2,
    clasificacionSisimo=clasificacionSismo_data[1],
    magnitud=MagnitudRichter(),
    origenDeGeneracion=origenDeGeneracion_data[2],
    alcanceSismo=alcanceSismo_data[0],
    estadoActual=estado_data[7],
    analistaSupervisor=empleado_data[2],
)

eventoSismico1._seriesTemporales = [serieTemporal_data[2]]

eventoSismico0._cambiosEstado = [cambioEstado_data[0]]

eventoSismico_data = [eventoSismico0, eventoSismico1]

# El eventoSismico0 posee las SeriesTemporales -> SerieTemporal0, SerieTemporal1
# y posee el cambio de estado CambioEstado0
# El eventoSismico1 posee la Serie Temporal -> SerieTemporal2
# y posee el cambio de estado CambioEstado1
# Tener en cuenta puesto que esto depende de su latitud y longitud y las fechas y los estados actuales!
