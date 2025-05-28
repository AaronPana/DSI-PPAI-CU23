from entities.TipoDeDato import TipoDeDato


class DetalleMuestraSismica:

    def __init__(self, tipoDeDato: TipoDeDato, valor) -> None:
        self._tipoDeDato: TipoDeDato = tipoDeDato
        # El tipo del valor va a depender de "tipoDeDato"
        self._valor = valor

    def getDatos(self) -> str:
        """
        rtype: str
        return: valor y tipo de dato
        """
        nombreUnidad: str = self._tipoDeDato.nombreUnidadMedida
        return f"{self._valor} {nombreUnidad}"
