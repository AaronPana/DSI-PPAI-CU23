class TipoDeDato:

    def __init__(
        self, denominacion: str, nombreUnidadMedida: str, valorUmbral: tuple[int, int]
    ) -> None:
        self._denominacion: str = denominacion
        self._nombreUnidadMedida: str = nombreUnidadMedida
        self._valorUmbral: tuple[int, int] = valorUmbral

    #Metodos utilizados en el CU23

    @property
    def denominacion(self) -> str:
        return self._denominacion

    # Metodo que retorna los datos necesarios a "DetalleMuestraSismica" para mostrar por pantalla
    @property
    def nombreUnidadMedida(self) -> str:
        return self._nombreUnidadMedida

    def esTuDenominacion(self, denomicacion: str) -> bool:
        return self._denominacion == denomicacion

    def getDatos(self) -> dict[str, str]:
        return {
            "denominacion": self._denominacion,
            "nombreUnidadMedida": self._nombreUnidadMedida,
        }
    
    #Métodos de acceso (getters y setters)

    @property
    def denominacion(self) -> str:
        return self._denominacion
    
    @denominacion.setter
    def denominacion(self, nuevaDenominacion: str) -> None:
        self._denominacion = nuevaDenominacion

    @property
    def nombreUnidadMedida(self) -> str:
        return self._nombreUnidadMedida
    
    @nombreUnidadMedida.setter
    def nombreUnidadMedida(self, nuevoNombreUnidadMedida: str) -> None:
        self._nombreUnidadMedida = nuevoNombreUnidadMedida
    
    @property
    def valorUmbral(self) -> tuple[int, int]:
        return self._valorUmbral
    
    @valorUmbral.setter
    def valorUmbral(self, nuevoValorUmbral: tuple[int, int]) -> None:
        self._valorUmbral = nuevoValorUmbral