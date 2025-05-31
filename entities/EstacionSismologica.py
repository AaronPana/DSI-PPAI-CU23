from datetime import date


class EstacionSismologica:

    def __init__(
        self,
        codigoEstacion: str,
        documentoCertificacionAdq: str,
        fechaSolicitudCertificacion: date,
        latitud: float,
        longitud: float,
        nombre: str,
        nroCertificacionAdquisicion: int,
    ) -> None:
        self._codigoEstacion: str = codigoEstacion
        self._documentoCertificacionAdq: str = documentoCertificacionAdq
        self._fechaSolicitudCertificacion: date = fechaSolicitudCertificacion
        self._latitud: float = latitud
        self._longitud: float = longitud
        self._nombre: str = nombre
        self._nroCertificacionAdquisicion: int = nroCertificacionAdquisicion

    @property
    def codigoEstacion(self) -> str:
        return self._codigoEstacion

    @property
    def nombre(self) -> str:
        return self._nombre
