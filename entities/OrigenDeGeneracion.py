class OrigenDeGeneracion:

    def __init__(self, descripcion: str, nombre: str) -> None:
        self._descripcion: str = descripcion
        self._nombre: str = nombre

    # Metodos utilizados en el CU23

    @property
    def nombre(self) -> str:
        return self._nombre

    # Métodos de acceso (getters y setters)

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self._nombre = nuevoNombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nuevaDescripcion: str) -> None:
        self._descripcion = nuevaDescripcion
