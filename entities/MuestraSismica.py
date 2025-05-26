from datetime import datetime
from entities.DetalleMuestraSismica import DetalleMuestraSismica


class MuestraSismica:

    def __init__(self, fechaHoraMuestra: datetime) -> None:
        self._fechaHoraMuestra: datetime = fechaHoraMuestra
        self._detallesMuestraSismica: list[DetalleMuestraSismica] = []

    def getDatos(self):
        pass

    # Acá se implementa la lógica de creación de detalles
    # y se agregan a al atributo "_detallesMuestraSismica"
    def crearDetalleMuestraSismica(self):
        pass
