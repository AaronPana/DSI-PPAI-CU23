from entities.TipoDeDato import TipoDeDato

TipoDeDato0 = TipoDeDato(
    denomicacion="Velocidad de onda",
    nombreUnidadMedida="Km/seg",
    valorUmbral=tuple[2, 9],
)

TipoDeDato1 = TipoDeDato(
    denomicacion="Frecuencia de onda",
    nombreUnidadMedida="Hz",
    valorUmbral=tuple[0, 50],
)

TipoDeDato2 = TipoDeDato(
    denomicacion="Longitud",
    nombreUnidadMedida="Km/ciclo",
    valorUmbral=tuple[0, 100],
)

tipoDeDato_data = [TipoDeDato0, TipoDeDato1, TipoDeDato2]

        # self._denominacion: str = denominacion
        # self._nombreUnidadMedida: str = nombreUnidadMedida
        # self._valorUmbral: tuple[int, int] = valorUmbral


# denominacion: Este atributo almacena el nombre descriptivo del tipo de dato sísmico. Por ejemplo,
# puede ser "Velocidad de onda", "Frecuencia de onda", o "Longitud". La clase incluye un método
# esTuDenominacion() y getDenominacion() relacionado con este atributo.

# nombreUnidadMedida: Guarda el nombre de la unidad de medida asociada a este tipo de dato. Siguiendo los
# ejemplos anteriores, sería "Km/seg" para la velocidad de onda, "Hz" para la frecuencia de onda, o "Km/ciclo"
# para la longitud.

# valorUmbral: Representa un valor de umbral configurable por el sistema para este tipo de dato.
# El sistema permite configurar umbrales personalizados para cada tipo de dato sísmico, independientemente
# de los umbrales configurados en los sismógrafos. Este umbral es relevante para detectar condiciones de alarma
# cuando los valores de las muestras superan dicho umbral.