class GestorGenerarSismograma:
    _sismograma: str = "src/data/images/sismograma.png"

    def __init__(self) -> None:
        pass

    @staticmethod
    def generarSismograma() -> str:
        return GestorGenerarSismograma._sismograma
