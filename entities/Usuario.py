from entities.Empleado import Empleado
from entities.Perfil import Perfil
from entities.Suscripcion import Suscripcion


class Usuario:

    def __init__(
        self,
        contraseña: str,
        nombreUsuario: str,
        empleado: Empleado,
        suscripcion: Suscripcion | None = None,
    ) -> None:
        self._contraseña: str = contraseña
        self._nombreUsuario: str = nombreUsuario
        self._empleado: Empleado = empleado
        self._suscripcion: Suscripcion | None = suscripcion
        # Asi modelamos nuestra relacion de asociacion 1..*
        self._perfiles: list[Perfil] = [Perfil()]

    # Metodos utilizados en el CU23

    # Es necesario importar Empleado como responsable de inscripcion, hay que hacer bien esto
    def getRILogueado(self) -> Empleado:
        return self._empleado

    # Métodos de acceso (getters y setters)

    @property
    def contraseña(self) -> str:
        return self._contraseña

    @contraseña.setter
    def contraseña(self, nuevaContraseña: str) -> None:
        self._contraseña = nuevaContraseña

    @property
    def nombreUsuario(self) -> str:
        return self._nombreUsuario

    @nombreUsuario.setter
    def nombreUsuario(self, nuevoNombreUsuario: str) -> None:
        self._nombreUsuario = nuevoNombreUsuario

    @property
    def empleado(self) -> Empleado:
        return self._empleado

    @empleado.setter
    def empleado(self, nuevoEmpleado: Empleado) -> None:
        self._empleado = nuevoEmpleado

    @property
    def suscripcion(self) -> Suscripcion | None:
        return self._suscripcion

    @suscripcion.setter
    def suscripcion(self, nuevaSuscripcion: Suscripcion | None) -> None:
        self._suscripcion = nuevaSuscripcion

    @property
    def perfiles(self) -> list[Perfil]:
        return self._perfiles

    @perfiles.setter
    def perfiles(self, nuevoPerfiles: list[Perfil]) -> None:
        self._perfiles = nuevoPerfiles
