from entities.Empleado import Empleado
from entities.Rol import Rol

Empleado0 = Empleado(
    nombre="Jorge",
    apellido="Perez",
    mail="perez_jorge@gmail.com",
    telefono="321 3456778",
    rol=Rol(),
)
Empleado1 = Empleado(
    nombre="Marcelo",
    apellido="Gomez",
    mail="gomez_marcelo@gmail.com",
    telefono="351 6749553",
    rol=Rol(),
)
Empleado2 = Empleado(
    nombre="Federica",
    apellido="Sanchez",
    mail="sanchez_federica@gmail.com",
    telefono="351 9450224",
    rol=Rol(),
)

empleado_data = [Empleado0, Empleado1, Empleado2]
