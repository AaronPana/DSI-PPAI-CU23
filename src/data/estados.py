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
Estado11 = Estado(ambito="SERIE_TEMPORAL", nombreEstado="TRANSMITIDA")

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
    Estado11
]