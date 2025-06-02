class ClasificacionSismo:

    def __init__(
        self, kmProfundidadDesde: int,
        kmProfundidadHasta: int,
        nombre: str
    ) -> None:
        self._kmProfundidadDesde: int = kmProfundidadDesde
        self._kmProfundidadHasta: int = kmProfundidadHasta
        self._nombre: str = nombre

    #Metodos utilizados en el CU23
    
    @property
    def nombre(self) -> str:
        return self._nombre

    #Métodos de acceso (getters y setters)

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self._nombre = nuevoNombre

    @property
    def kmProfundidadDesde(self) -> int:
        return self._kmProfundidadDesde
    
    @kmProfundidadDesde.setter
    def kmProduncidadDesde(self, nuevaKmProdundidadDesde: int) -> None:
        self._kmProfundidadDesde = nuevaKmProdundidadDesde
    
    @property
    def kmProfundidadHasta(self) -> int:
        return self._kmProfundidadHasta
    
    @kmProfundidadHasta.setter
    def kmProfundidadHasta(self, nuevaKmProfundidadHasta: int) -> None:
        self._nuevaKmProfundidadHasta = nuevaKmProfundidadHasta