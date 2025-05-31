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

# nombre: Representa el nombre de la clasificación de profundidad del sismo. Nombres
# mencionados en las fuentes son "sismos superficiales", "intermedios" o "profundos".

# kmProfundidadDesde: Indica el límite inferior del rango de profundidad (en kilómetros) que define esta
# clasificación. Para "sismos superficiales" sería 0 km, para "intermedios" sería 61 km y para
# "profundos" sería 301 km.

# kmProfundidadHasta: Indica el límite superior del rango de profundidad (en kilómetros) que define
# esta clasificación. Para "sismos superficiales" sería 60 km, para "intermedios" sería 300 km y para
# "profundos" sería 650 km.