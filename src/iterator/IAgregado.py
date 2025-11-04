class IAgregado:
    @staticmethod
    def crearIterador(listaElementos: list) -> object:
        if not listaElementos:
            return None

        # Importaciones aquí para romper el ciclo
        from entities.EventoSismico import EventoSismico
        from entities.SerieTemporal import SerieTemporal
        from entities.MuestraSismica import MuestraSismica
        from entities.DetalleMuestraSismica import DetalleMuestraSismica

        from iterator.IIteradorEventosSismicos import IteradorEventosSismicos
        from iterator.IIteradorSeriesTemporales import IteradorSeriesTemporales
        from iterator.IIteradorMuestrasSismicas import IteradorMuestrasSismicas
        from iterator.IIteradorDetallesMuestraSismica import IteradorDetallesMuestraSismica

        primerElemento = listaElementos[0]

        if isinstance(primerElemento, EventoSismico):
            return IteradorEventosSismicos(listaElementos)
        elif isinstance(primerElemento, SerieTemporal):
            return IteradorSeriesTemporales(listaElementos)
        elif isinstance(primerElemento, MuestraSismica):
            return IteradorMuestrasSismicas(listaElementos)
        elif isinstance(primerElemento, DetalleMuestraSismica):
            return IteradorDetallesMuestraSismica(listaElementos)
        else:
            raise TypeError("Tipo de lista no soportado para crear iterador.")