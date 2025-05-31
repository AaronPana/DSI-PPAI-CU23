from estados_diccionario import estados_data

class Estado:

    def __init__(self, ambito: str, nombreEstado: str) -> None:
        self._ambito: str = ambito
        self._nombreEstado: str = nombreEstado

    def esAmbitoEventoSismico(self) -> bool:
        return self._ambito == "EVENTO_SISMICO"

    def esAutoDetectado(self) -> bool:
        return (self._ambito == "EVENTO_SISMICO") and (self._nombreEstado == "AUTODETECTADO")

    def esPendienteRevision(self) -> bool:
        return (self._ambito == "EVENTO_SISMICO") and (self._nombreEstado == "PENDIENTE_REVISION")

    def esBloqueadoEnRevision(self) -> bool:
        return (self._ambito == "EVENTO_SISMICO") and (self._nombreEstado == "BLOQUEADO_REVISION")

    def esRechazado(self) -> bool:
        return (self._ambito == "EVENTO_SISMICO") and (self._nombreEstado == "RECHAZADO")
