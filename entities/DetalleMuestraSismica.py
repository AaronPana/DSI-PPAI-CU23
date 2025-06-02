from entities.TipoDeDato import TipoDeDato

class DetalleMuestraSismica:

    def __init__(self, tipoDeDato: TipoDeDato, valor: float) -> None:
        self._tipoDeDato: TipoDeDato = tipoDeDato
        self._valor: float = valor

    #Metodos utilizados en el CU27

    def getDatos(self) -> dict[str, str]:
        """
        rtype: dict[str, str]
        return: denominacion, valor y tipo de dato
        """
        infoTipoDeDato = self._tipoDeDato.getDatos()
        infoDetalle = {
            "denominacion": infoTipoDeDato["denominacion"],
            "valor": str(self._valor),
            "nombreUnidadMedida": infoTipoDeDato["nombreUnidadMedida"],
        }
        return infoDetalle

    #Métodos de acceso (getters y setters)

    @property
    def tipoDeDato(self) -> TipoDeDato:
        return self._tipoDeDato
    
    @tipoDeDato.setter
    def tipoDeDato(self, nuevoTipoDeDato: TipoDeDato) -> None:
        self._tipoDeDato = nuevoTipoDeDato

    @property
    def valor(self) -> float:
        return self._valor
    
    @valor.setter
    def valor(self, nuevoValor: float) -> None:
        self._valor = nuevoValor
