from entities.TipoDeDato import TipoDeDato

TipoDeDato0 = TipoDeDato(
    denominacion="Velocidad de onda",
    nombreUnidadMedida="Km/seg",
    valorUmbral=(2, 9),
)

TipoDeDato1 = TipoDeDato(
    denominacion="Frecuencia de onda",
    nombreUnidadMedida="Hz",
    valorUmbral=(0, 50),
)

TipoDeDato2 = TipoDeDato(
    denominacion="Longitud",
    nombreUnidadMedida="Km/ciclo",
    valorUmbral=(0, 100),
)

tipoDeDato_data = [TipoDeDato0, TipoDeDato1, TipoDeDato2]