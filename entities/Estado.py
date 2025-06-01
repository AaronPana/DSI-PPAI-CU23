class Estado:

    def __init__(self, ambito: str, nombreEstado: str) -> None:
        self._ambito: str = ambito
        self._nombreEstado: str = nombreEstado

    #Metodos utilizados en el CU23

    def esAmbitoEventoSismico(self) -> bool:
        return self._ambito == "EVENTO_SISMICO"

    def esAutoDetectado(self) -> bool:
        return self._nombreEstado == "AUTODETECTADO"

    def esPendienteRevision(self) -> bool:
        return self._nombreEstado == "PENDIENTE_REVISION"

    def esBloqueadoEnRevision(self) -> bool:
        return self._nombreEstado == "BLOQUEADO_REVISION"

    def esRechazado(self) -> bool:
        return self._nombreEstado == "RECHAZADO"

    #Métodos de acceso (getters y setters)

    @property
    def ambito(self) -> str:
        return self._ambito
    
    @ambito.setter
    def ambito(self, nuevoAmbito: str) -> None:
        self._ambito = nuevoAmbito
    
    @property
    def nombreEstado(self) -> str:
        return self._nombreEstado
    
    @nombreEstado.setter
    def nombreEstado(self, nuevoNombreEstado: str) -> None:
        self._nombreEstado = nuevoNombreEstado