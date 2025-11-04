class GestorGenerarSismograma:
    _sismograma: str = "../data/sismograma.png"

    def __init__(self) -> None:
        pass

    @staticmethod
    def generarSismograma() -> str:
        return GestorGenerarSismograma._sismograma
