from entities.Usuario import Usuario
from empleados import empleado_data

usuario0 = Usuario(contraseña="1234", nombreUsuario="Jorge", empleado=empleado_data[0], suscripcion=None)
usuario1 = Usuario(contraseña="1234", nombreUsuario="Marcelo", empleado=empleado_data[1], suscripcion=None)
usuario2 = Usuario(contraseña="1234", nombreUsuario="Federica", empleado=empleado_data[2], suscripcion=None)

usuario_data = [usuario0, usuario1, usuario2]