class Estado:

    def __init__(self, ambito: str, nombreEstado: str) -> None:
        self._ambito: str = ambito
        self._nombreEstado: str = nombreEstado

    def esAutoDetectado(self):
        pass

    def esPendienteRevision(self):
        pass

    def esAmbitoEventoSismico(self):
        pass

    def esBloqueadoEnRevision(self):
        pass

    def esRechazado(self):
        pass
