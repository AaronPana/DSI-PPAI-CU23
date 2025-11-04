from data.empleados import empleado_data
from entities.Suscripcion import Suscripcion
from entities.Usuario import Usuario

usuario0 = Usuario(
    contraseña="1234",
    nombreUsuario="Jorge",
    empleado=empleado_data[0],
    suscripcion=Suscripcion(),
)

usuario1 = Usuario(
    contraseña="1234",
    nombreUsuario="Marcelo",
    empleado=empleado_data[1],
    suscripcion=Suscripcion(),
)

usuario2 = Usuario(
    contraseña="1234",
    nombreUsuario="Federica",
    empleado=empleado_data[2],
    suscripcion=Suscripcion(),
)

usuario_data: list[Usuario] = [usuario0, usuario1, usuario2]
