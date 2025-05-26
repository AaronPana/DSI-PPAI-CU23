from entities.Rol import Rol


class Empleado:
    def __init__(
        self, apellido: str, mail: str, nombre: str, telefono: str, rol: Rol
    ) -> None:
        self._apellido: str = apellido
        self._mail: str = mail
        self._nombre: str = nombre
        self._telefono: str = telefono
        self._rol: Rol = rol

    @property
    def mail(self) -> str:
        return self._mail

    # Asumo que se debe acceder a este dato mediante rol:Rol
    # pero como no lo modelamos, lo dejo con un pass
    def esResponsableDeReparacion(self):
        pass
