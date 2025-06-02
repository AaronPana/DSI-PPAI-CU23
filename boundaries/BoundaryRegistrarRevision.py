import flet as ft

class BoundaryRegistrarRevision:

    def __init__(self, page: ft.Page) -> None:
        self._page: ft.Page = page
        #self._gestorRegistrarRevision: GestorRegistrarRevision = (
        #    GestorRegistrarRevision(self, datetime.now())
        #)
        self._grillaEventosSismicosNoRevisados: ft.DataTable = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Fecha y Hora de Ocurrencia")),
                ft.DataColumn(label=ft.Text("Latitud Epicentro")),
                ft.DataColumn(label=ft.Text("Longitud Epicentro")),
                ft.DataColumn(label=ft.Text("Latitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Longitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Magnitud")),
                ft.DataColumn(label=ft.Text("Clasificación")),
                ft.DataColumn(label=ft.Text("Origen Generación")),
                ft.DataColumn(label=ft.Text("Alcance")),
            ],
            rows=[],
            heading_row_color=ft.Colors.BLUE_800
        )

        self._btnSeleccionarEventoSismicoNoRevisado = None #no hay ?
        self._grillaEventoSismicoSeleccionado = None # como no use una grilla, habria que eliminarla
        self._btnVisualizarMapa = None
        self._btnModificarDatosEventoSismico = None
        self._campoAccionRevision = None
        # Simulacion de datos
        self._eventosSismicosNoRevisados = [
            {
                "fechaHoraOcurrencia": "2025-05-28 14:30:00",
                "latitudEpicentro": "-31.4201",
                "longitudEpicentro": "-64.1888",
                "latitudHipocentro": "-31.4190",
                "longitudHipocentro": "-64.1895",
                "valorMagnitud": "5.6",
                "clasificacion": "Intermedio",
                "origenDeGeneracion": "Sismo interplaca",
                "alcanceSismico": "Regional"
            },
            {
                "fechaHoraOcurrencia": "2025-05-27 03:45:12",
                "latitudEpicentro": "-32.0123",
                "longitudEpicentro": "-63.1234",
                "latitudHipocentro": "-32.0101",
                "longitudHipocentro": "-63.1256",
                "valorMagnitud": "3.9",
                "clasificacion": "Superficial",
                "origenDeGeneracion": "Sismo volcánico",
                "alcanceSismico": "Local"
            }
        ]

        self._eventosDerivados = [
            {
                "fechaHoraOcurrencia": "2025-05-30 09:12:45",
                "latitudEpicentro": "-30.9472",
                "longitudEpicentro": "-66.1234",
                "latitudHipocentro": "-30.9450",
                "longitudHipocentro": "-66.1201",
                "valorMagnitud": "4.8",
                "clasificacion": "Intermedio",
                "origenDeGeneracion": "Sismo cortical",
                "alcanceSismico": "Regional"
            },
            {
                "fechaHoraOcurrencia": "2025-05-29 22:01:10",
                "latitudEpicentro": "-33.1230",
                "longitudEpicentro": "-65.7890",
                "latitudHipocentro": "-33.1211",
                "longitudHipocentro": "-65.7902",
                "valorMagnitud": "6.2",
                "clasificacion": "Profundo",
                "origenDeGeneracion": "Sismo de subducción",
                "alcanceSismico": "Internacional"
            }
        ]

        #seccion: detalle de evento sismico
        self.campos_evento = {}
        self.formulario_edicion = ft.Column(visible=False)
        self.evento_original = None

        self.nombres_campos = [
            "Fecha", "Hora", "Latitud", "Longitud",
            "Profundidad", "Magnitud", "Alcance", "Estado"
        ]

        for campo in self.nombres_campos:
            self.campos_evento[campo] = ft.TextField(
                label=campo,
                disabled=True,
                expand=True
            )
        
        
        self.imagen_mapa = ft.Image(
            key="mapaSismograma",
            src="https://picsum.photos/400/250",  
            visible=False,
            width=400,
            height=250,
            fit=ft.ImageFit.CONTAIN,
        )

        self.texto_mapa = ft.Text(
            "Mapa Sísmico",
            size=16,
            weight="bold",
            color=ft.Colors.BLUE_800,
            text_align=ft.TextAlign.CENTER
        )

        self.contenedor_mapa = ft.Container(
            content=ft.Column([
                self.texto_mapa,
                ft.Container(  # Contenedor interno para centrar la imagen
                    content=self.imagen_mapa,
                    alignment=ft.alignment.center,  
                    expand=True
                )
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            spacing=10
            ),
            width=420,
            height=300, 
            bgcolor=ft.Colors.GREY_100,
            border_radius=10,
            padding=15,
            alignment=ft.alignment.center, 
            visible=False  
        )
        #Botones
        boton_modificar = ft.ElevatedButton("Modificar evento", on_click=self.modificarEvento)
        boton_guardar = ft.ElevatedButton("Guardar cambios", on_click=self.guardarCambiosEvento)
        boton_cancelar = ft.ElevatedButton("Cancelar cambios", on_click=self.cancelarCambiosEvento)
        boton_ver_mapa = ft.ElevatedButton("Ver mapa", on_click=self.mostrarSismograma)

        # Sección detalle evento
        self.formulario_edicion = ft.Column([

            ft.Text("Detalles del evento sísmico seleccionado", size=20, weight="bold"),
            ft.Row([
                #Columna izquierda
                ft.Column([
                    *[self.campos_evento[campo] for campo in self.nombres_campos],
                    ft.Row([
                        boton_modificar,
                        boton_guardar,
                        boton_cancelar,
                        boton_ver_mapa
                    ])
                ], expand=1),
                #Columna derecha
                ft.Column([
                    self.contenedor_mapa
                ], expand=1)
            ])
        ], visible=False)

        #Seccion evento derivado y dropdown
        self._dropdownAccionRevision = ft.Dropdown(
            label="Acción de revisión",
            options=[
                ft.dropdown.Option("Aceptar Evento"),
                ft.dropdown.Option("Rechazar Evento"),
                ft.dropdown.Option("Derivar a experto")
            ],
            width=300
        )

        self._btnRegistrarAccion = ft.ElevatedButton(
            text="Registrar",
            on_click=self.tomarSeleccionRevision
        )
    
        self._grillaEventosDerivados = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Fecha y Hora de Ocurrencia")),
                ft.DataColumn(label=ft.Text("Latitud Epicentro")),
                ft.DataColumn(label=ft.Text("Longitud Epicentro")),
                ft.DataColumn(label=ft.Text("Latitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Longitud Hipocentro")),
                ft.DataColumn(label=ft.Text("Magnitud")),
                ft.DataColumn(label=ft.Text("Clasificación")),
                ft.DataColumn(label=ft.Text("Origen Generación")),
                ft.DataColumn(label=ft.Text("Alcance")),
            ],
        rows=[],
        heading_row_color=ft.Colors.BLUE_100
        )

        self.formulario_revision_final = ft.Column([
            ft.Text("Eventos derivados al experto", size=20, weight="bold"),
            self._grillaEventosDerivados,
            ft.Row([self._dropdownAccionRevision, self._btnRegistrarAccion])
            ], visible=True)

    
    #Ventana
    def registrarRevisionManual(self):
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.title = "Red Sísmica"
        self._page.scroll = ft.ScrollMode.AUTO
        self._page.window.width = 1300
        self._page.window.height = 760
        self._page.window.resizable = False

        self.cargarEventosSismicos(self._eventosSismicosNoRevisados)
        self.cargarEventosDerivados()

        self._page.add(
            self._grillaEventosSismicosNoRevisados,
            self.formulario_edicion,
            self.formulario_revision_final  
            )

    def habilitarVentana(self):
        pass

    # cambiar datos de celdas por "objeto.atributo"
    def cargarEventosSismicos(self, eventos):
        filas: list[ft.DataRow] = []
        for index, evento in enumerate(eventos):
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(evento["fechaHoraOcurrencia"]))),
                    ft.DataCell(ft.Text(str(evento["latitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["latitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["valorMagnitud"]))),
                    ft.DataCell(ft.Text(str(evento["clasificacion"]))),
                    ft.DataCell(ft.Text(str(evento["origenDeGeneracion"]))),
                    ft.DataCell(ft.Text(str(evento["alcanceSismico"]))),
                ],
                selected=False,
                on_select_changed=lambda selected, i=index: self._onSelectRow(i, selected)
            )
            filas.append(fila)

        self._grillaEventosSismicosNoRevisados.rows = filas
    
    def _onSelectRow(self, index, selected):    
            if selected:
                for i, row in enumerate(self._grillaEventosSismicosNoRevisados.rows):

                    row.selected = (i == index)

                evento = self._eventosSismicosNoRevisados[index]

        # Mapea las claves del diccionario a los nombres esperados por el formulario
            evento_formateado = {
                "Fecha": evento["fechaHoraOcurrencia"].split(" ")[0],
                "Hora": evento["fechaHoraOcurrencia"].split(" ")[1],
                "Latitud": evento["latitudEpicentro"],
                "Longitud": evento["longitudEpicentro"],
                "Profundidad": evento.get("latitudHipocentro", ""), 
                "Magnitud": evento["valorMagnitud"],
                "Alcance": evento["alcanceSismico"],
                "Estado": evento["clasificacion"]
            }

            self.eventoSeleccionado(evento_formateado)
            self._page.update()


    # metodos detalle evento

    def eventoSeleccionado(self, evento_dict):
        self.evento_original = evento_dict.copy()

        for campo in self.nombres_campos:
            self.campos_evento[campo].value = str(evento_dict.get(campo, ""))

            # reiniciar estado de los campos (deshabilitar todos)
            self.campos_evento[campo].disabled = True
        
        self.contenedor_mapa.visible = False
        self.imagen_mapa.visible = False

        self.formulario_edicion.visible = True
        self._page.update()
    
    def modificarEvento(self, e):
        for campo in self.nombres_campos:
            self.campos_evento[campo].disabled = False
        
        self._page.update()
    
    def guardarCambiosEvento(self, e):
        datos_actualizados = {
            campo: self.campos_evento[campo].value
            for campo in self.nombres_campos
        }

        for campo in self.nombres_campos:
            self.campos_evento[campo].disabled = True

        self._page.update()

    def cancelarCambiosEvento(self, e):
        for campo in self.nombres_campos:
            self.campos_evento[campo].value = str(self.evento_original.get(campo, ""))
            self.campos_evento[campo].disabled = True
        self._page.update()

    # metodos ultima seccion
    def cargarEventosDerivados(self):
        filas: list[ft.DataRow] = []
        for evento in self._eventosDerivados:
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(evento["fechaHoraOcurrencia"]))),
                    ft.DataCell(ft.Text(str(evento["latitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudEpicentro"]))),
                    ft.DataCell(ft.Text(str(evento["latitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["longitudHipocentro"]))),
                    ft.DataCell(ft.Text(str(evento["valorMagnitud"]))),
                    ft.DataCell(ft.Text(str(evento["clasificacion"]))),
                    ft.DataCell(ft.Text(str(evento["origenDeGeneracion"]))),
                    ft.DataCell(ft.Text(str(evento["alcanceSismico"]))),
                ],
            )
            filas.append(fila)
        self._grillaEventosDerivados.rows = filas

    def tomarSeleccionRevision(self, e):
        accion = self._dropdownAccionRevision.value
        if accion == "Aceptar Evento":
            print("Evento aceptado.")
        elif accion == "Rechazar Evento":
            print("Evento rechazado.")
        else:
            print("Evento derivado a experto.")
    

    # metodos
    def mostrarDatosEventosSismicos(self):
        pass

    def seleccionEventoSismico(self):
        pass
    
    def mostrarDatosEventoSismico(self):
        pass

    def mostrarSismograma(self, e):
        self.contenedor_mapa.visible = True
        self.imagen_mapa.visible = True
        
        self._page.update()

    def habilitarOpcionVisualizarMapa(self):#no van ?
        pass

    def habilitarBtnMapa(self):# no van?
        pass

    def habilitarModificarDatosEventoSismico(self): #no van?
        pass

    def solicitarAccionRevision(self):
        pass
