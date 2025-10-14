from entities.OrigenDeGeneracion import OrigenDeGeneracion

origenDeGeneracion0 = OrigenDeGeneracion(
    nombre="Sismo Interplaca",
    descripcion="Terremoto que ocurre dentro de una placa tectónica, en lugar de en el límite entre dos placas.",
)
origenDeGeneracion1 = OrigenDeGeneracion(
    nombre="Sismo Volcanico",
    descripcion="Temblor de tierra provocado por la actividad volcánica.",
)
origenDeGeneracion2 = OrigenDeGeneracion(
    nombre="Sismo provocado por explosiones de minas",
    descripcion="Se induce como resultado de actividades mineras.",
)

origenDeGeneracion_data = [
    origenDeGeneracion0,
    origenDeGeneracion1,
    origenDeGeneracion2,
]
