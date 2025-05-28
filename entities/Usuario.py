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

    # Es necesario importar Empleado como responsable de inscripcion, hay que hacer bien esto
    def getRILogueado(self) -> Empleado:
        return self._empleado
