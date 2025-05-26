class TipoDeDato:

    def __init__(
        self, denominacion: str, nombreUnidadMedida: str, valorUmbral: str
    ) -> None:
        self._denominacion: str = denominacion
        self._nombreUnidadMedida: str = nombreUnidadMedida
        self._valorUmbral: str = valorUmbral

    @property
    def denominacion(self) -> str:
        return self._denominacion

    def getDatos(self):
        pass

    def esTuDenominacion(self):
        pass
