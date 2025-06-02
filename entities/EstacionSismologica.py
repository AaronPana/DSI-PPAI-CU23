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

    #Metodos utilizados en el CU23

    @property
    def codigoEstacion(self) -> str:
        return self._codigoEstacion

    @property
    def nombre(self) -> str:
        return self._nombre

    #Métodos de acceso (getters y setters)

    @codigoEstacion.setter
    def codigoEstacion(self, nuevoCodigoEstacion: str) -> None:
        self._codigoEstacion = nuevoCodigoEstacion
    
    @property
    def documentoCertificacionAdq(self) -> str:
        return self._documentoCertificacionAdq
    
    @documentoCertificacionAdq.setter
    def documentoCertificacionAdq(self, nuevoDocumentoCertificacionAdq: str) -> None:
        self._documentoCertificacionAdq = nuevoDocumentoCertificacionAdq
    
    @property
    def fechaSolicitudCertificacion(self) -> date:
        return self._fechaSolicitudCertificacion
    
    @fechaSolicitudCertificacion.setter
    def fechaSolicitudCertificacion(self, nuevoFechaSolicitudCertificacion: date) -> None:
        self._fechaSolicitudCertificacion = nuevoFechaSolicitudCertificacion
    
    @property
    def latitud(self) -> float:
        return self._latitud
    
    @latitud.setter
    def latitud(self, nuevaLatitud: float) -> None:
        self._latitud = nuevaLatitud
    
    @property
    def longitud(self) -> float:
        return self._longitud
    
    @longitud.setter
    def longitud(self, nuevaLongitud: float) -> None:
        self._longitud = nuevaLongitud
    
    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self._nombre = nuevoNombre

    @property
    def nroCertificacionAdquisicion(self) -> int:
        return self._nroCertificacionAdquisicion

    @nroCertificacionAdquisicion.setter
    def nroCertificacionAdquisicion(self, nuevoNroCertificacionAdquisicion: int) -> None:
        self._nroCertificacionAdquisicion = nuevoNroCertificacionAdquisicion