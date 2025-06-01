from entities.TipoDeDato import TipoDeDato


class DetalleMuestraSismica:

    def __init__(self, tipoDeDato: TipoDeDato, valor: float) -> None:
        self._tipoDeDato: TipoDeDato = tipoDeDato
        # El tipo del valor va a depender de "tipoDeDato"
        self._valor: float = valor

    def getDatos(self) -> dict[str, str]:
        """
        rtype: str
        return: valor y tipo de dato
        """
        infoTipoDeDato = self._tipoDeDato.getDatos()
        infoDetalle = {
            "denominacion": infoTipoDeDato["denominacion"],
            "valor": str(self._valor),
            "nombreUnidadMedida": infoTipoDeDato["nombreUnidadMedida"],
        }
        return infoDetalle
