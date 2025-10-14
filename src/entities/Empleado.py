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

    # Metodos utilizados en el CU23

    @property
    def mail(self) -> str:
        return self._mail

    # Asumo que se debe acceder a este dato mediante rol:Rol
    # pero como no lo modelamos, lo dejo con un pass
    def esResponsableDeReparacion(self):
        pass

    # Métodos de acceso (getters y setters)

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, nuevoApellido: str) -> None:
        self._apellido = nuevoApellido

    @mail.setter
    def mail(self, nuevoMail: str) -> None:
        self._mail = nuevoMail

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self._nombre = nuevoNombre

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, nuevoTelefono: str) -> None:
        self._telefono = nuevoTelefono

    @property
    def rol(self) -> Rol:
        return self._rol

    @rol.setter
    def rol(self, nuevoRol: Rol) -> None:
        self._rol = nuevoRol
