class OrigenDeGeneracion:

    def __init__(self, descripcion: str, nombre: str) -> None:
        self._descripcion: str = descripcion
        self._nombre: str = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
