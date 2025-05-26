from entities.TipoDeDato import TipoDeDato


class DetalleMuestraSismica:

    def __init__(self, tipoDeDato: TipoDeDato, valor) -> None:
        self._tipoDeDato: TipoDeDato = tipoDeDato
        self.valor = valor

    def getDatos(self):
        pass
