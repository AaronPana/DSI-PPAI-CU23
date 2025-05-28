class TipoDeDato:

    def __init__(
        self, denominacion: str, nombreUnidadMedida: str, valorUmbral: tuple[int, int]
    ) -> None:
        self._denominacion: str = denominacion
        self._nombreUnidadMedida: str = nombreUnidadMedida
        self._valorUmbral: tuple[int, int] = valorUmbral

    @property
    def denominacion(self) -> str:
        return self._denominacion

    # Metodo que retorna los datos necesarios a "DetalleMuestraSismica" para mostrar por pantalla
    @property
    def nombreUnidadMedida(self) -> str:
        return self._nombreUnidadMedida

    def esTuDenominacion(self, denomicacion: str) -> bool:
        return self._denominacion == denomicacion
