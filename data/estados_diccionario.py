estados_data = {
    "E1": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "AUTOCONFIRMADO",},
    
    "E2": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "AUTODETECTADO",}, #Se usara en el diagrama de secuencia
    
    "E3": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "PENDIENTE_REVISION",}, #Se usara en el diagrama de secuencia
    
    "E4": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "BLOQUEADO_REVISION",}, #Se usara en el diagrama de secuencia
    
    "E5": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "EN_REVISION",},
    
    "E6": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "REVISION_DERIVADA",},
    
    "E7": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "CONFIRMADO",},
    
    "E8": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "RECHAZADO",}, #Se usara en el diagrama de secuencia
    
    "E9": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "PENDIENTE_CIERRE",},
    
    "E10": {
    "ambito": "EVENTO_SISMICO",
    "nombreEstado": "CERRADO",},
}


# El atributo ambito en la clase Estado permite diferenciar a qué tipo de objeto(como un Evento Sísmico, un Sismógrafo, etc.)
# aplica una instancia particular de Estado, incluso si diferentes tipos de objetos pudieran tener estados con el mismo
# nombreEstado (aunque no se presentan ejemplos de nombres duplicados en los estados listados en las fuentes). El método
# esAmbitoEventoSismico() sería una forma de verificar si una instancia de Estado es aplicable a un EventoSismico.