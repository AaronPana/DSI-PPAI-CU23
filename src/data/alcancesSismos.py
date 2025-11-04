from entities.AlcanceSismo import AlcanceSismo

AlcanceSismo0 = AlcanceSismo(nombre="Sismo Local", descripcion="Hasta 100 km")

AlcanceSismo1 = AlcanceSismo(nombre="Sismo Regional", descripcion="Hasta 1000 km")

AlcanceSismo2 = AlcanceSismo(nombre="Tele Sismo", descripcion="Más de 1000 km")

alcanceSismo_data: list[AlcanceSismo] = [AlcanceSismo0, AlcanceSismo1, AlcanceSismo2]
