from entities.ClasificacionSismo import ClasificacionSismo

ClasificacionSismo0 = ClasificacionSismo(
    nombre="Sismo Superficial",
    kmProfundidadDesde=0,
    kmProfundidadHasta=60
)

ClasificacionSismo1 = ClasificacionSismo(
    nombre="Sismo Intermedio",
    kmProfundidadDesde=61,
    kmProfundidadHasta=300
)

ClasificacionSismo2 = ClasificacionSismo(
    nombre="Sismo Profundo",
    kmProfundidadDesde=301,
    kmProfundidadHasta=650
)

clasificacionSismo_data = [ClasificacionSismo0, ClasificacionSismo1, ClasificacionSismo2]