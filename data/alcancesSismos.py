from entities.AlcanceSismo import AlcanceSismo

AlcanceSismo0 = AlcanceSismo(
    nombre="Sismo Local",
    descripcion="Hasta 100 km"
)

AlcanceSismo1 = AlcanceSismo(
    nombre="Sismo Regional",
    descripcion="Hasta 1000 km"
)

AlcanceSismo2 = AlcanceSismo(
    nombre="Tele Sismo",
    descripcion="Más de 1000 km"
)

alcanceSismo_data = [AlcanceSismo0, AlcanceSismo1, AlcanceSismo2]

# nombre: Este atributo representa el nombre de la clasificación del alcance del sismo. Ejemplos proporcionados incluyen
# "sismos locales", "sismos regionales" o "tele sismos".
# descripcion: Este atributo proporciona una descripción o detalle de la clasificación. Para el alcance, la
# descripción detalla la distancia epicentral que define la categoría (por ejemplo, "hasta 100 km" para sismos
# locales, "hasta 1000 km" para sismos regionales, o "más de 1000 km" para tele sismos).