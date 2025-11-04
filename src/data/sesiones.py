from datetime import datetime

from data.usuarios import usuario_data
from entities.Sesion import Sesion

Sesion0 = Sesion(
    fechaHoraDesde=datetime.now(), fechaHoraHasta=None, usuario=usuario_data[2]
)
