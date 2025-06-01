from entities.Estado import Estado

Estado0 = Estado(ambito="SISMOGRAFO", nombreEstado="DISPONIBLE")
Estado1 = Estado(ambito="EVENTO_SISMICO", nombreEstado="AUTOCONFIRMADO")
Estado2 = Estado(ambito="EVENTO_SISMICO", nombreEstado="AUTODETECTADO")
Estado3 = Estado(ambito="EVENTO_SISMICO", nombreEstado="PENDIENTE_REVISION")
Estado4 = Estado(ambito="EVENTO_SISMICO", nombreEstado="BLOQUEADO_REVISION")
Estado5 = Estado(ambito="EVENTO_SISMICO", nombreEstado="EN_REVISION")
Estado6 = Estado(ambito="EVENTO_SISMICO", nombreEstado="REVISION_DERIVADA")
Estado7 = Estado(ambito="EVENTO_SISMICO", nombreEstado="CONFIRMADO")
Estado8 = Estado(ambito="EVENTO_SISMICO", nombreEstado="RECHAZADO")
Estado9 = Estado(ambito="EVENTO_SISMICO", nombreEstado="PENDIENTE_CIERRE")
Estado10 = Estado(ambito="EVENTO_SISMICO", nombreEstado="CERRADO")

estado_data = [
    Estado0,
    Estado1,
    Estado2,
    Estado3,
    Estado4,
    Estado5,
    Estado6,
    Estado7,
    Estado8,
    Estado9,
    Estado10,
]


# El atributo ambito en la clase Estado permite diferenciar a qué tipo de objeto(como un Evento Sísmico, un Sismógrafo, etc.)
# aplica una instancia particular de Estado, incluso si diferentes tipos de objetos pudieran tener estados con el mismo
# nombreEstado (aunque no se presentan ejemplos de nombres duplicados en los estados listados en las fuentes).
