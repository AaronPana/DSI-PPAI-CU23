class ClasificacionSismo:

    def __init__(
        self, kmProfundidadDesde: int, kmProfundidadHasta: int, nombre: str
    ) -> None:
        self._kmProfundidadDesde: int = kmProfundidadDesde
        self._kmProfundidadHasta: int = kmProfundidadHasta
        self._nombre: str = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
