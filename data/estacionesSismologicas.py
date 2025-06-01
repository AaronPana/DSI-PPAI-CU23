from datetime import datetime
from entities.EstacionSismologica import EstacionSismologica

EstacionSismologica0 = EstacionSismologica(
    codigoEstacion="001",
    documentoCertificacionAdq="certificacionAdquisicion2005.pdf",
    fechaSolicitudCertificacion=datetime(2005, 5, 30, 8, 30),
    latitud=-34.6037,
    longitud=-58.3816,
    nombre="Estacion Simologia Bs As NORTE",
    nroCertificacionAdquisicion=5567,
)

EstacionSismologica1 = EstacionSismologica(
    codigoEstacion="002",
    documentoCertificacionAdq="certificacionAdquisicion2003.pdf",
    fechaSolicitudCertificacion=datetime(2003, 5, 5, 8, 30),
    latitud=-34.6050,
    longitud=-58.3800,
    nombre="Estacion Simologia Bs As SUR",
    nroCertificacionAdquisicion=3563,
)


EstacionSismologica2 = EstacionSismologica(
    codigoEstacion="003",
    documentoCertificacionAdq="certificacionAdquisicion2012.pdf",
    fechaSolicitudCertificacion=datetime(2012, 5, 5, 8, 30),
    latitud=37.7749,
    longitud=-122.4194,
    nombre="Estacion Simologia San Francisco",
    nroCertificacionAdquisicion=3563,
)

estacionSismologica_data = [
    EstacionSismologica0,
    EstacionSismologica1,
    EstacionSismologica2,
]
