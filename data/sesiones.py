from entities.Sesion import Sesion
from datetime import datetime
from data.usuarios import usuario_data

Sesion0 = Sesion(fechaHoraDesde=datetime.now(), fechaHoraHasta=None, usuario=usuario_data[2])