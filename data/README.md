# DICCIONARIO
## Nomenclatura

### Nombrar el archivo
El archivo se nombrara con el mismo nombre de la clase en plural

Ejemplo: eventosSismicos.py

### Nombrar la variable de "retrno"

El diccionario en sí debe nombrarse utilizando el siguiente formato: nombreClase_data

Ejemplo: eventoSismico_data

### Nombrar los objetos
        
Cada registro tendrá un identificador generado a partir de las iniciales de la clase seguido de un número secuencial. Por ejemplo, para la clase EventoSismico, el identificador será el nombre de la clase en PascalCase más un número creciente: NombreClaseN 

Ejemplo: "AlcanceSismo1", "AlcanceSismo2", ..., "AlcanceSismoN".

### Datos de atributos

Cuando un atributo tipo nombre representa un valor constante que no debe modificarse, **del cual se debe ralizar una comparacion en codigo** —como el nombre de un estado, un tipo o una categoría fija— debe escribirse en mayúsculas, utilizando guiones bajos para separar palabras.

Ejemplo: "nombre": "SISMOS_LOCALES"

En cualquier otra parte se nombrara siguiendo las indicaciones del dominio

---

# Data

- [x] AlcanceSismo.py
- [x] CambioEstado.py
- [x] ClasificacionSismo.py
- [x] DetalleMuestraSismica.py
- [x] Empleado.py
- [x] EstacionSismologica.py
- [x] Estado.py
- [x] EventoSismico.py
- [x] MuestraSismica.py
- [x] SerieTemporal.py
- [ ] Sesion.py -> Se espera que se encuentre hardcodeada no se ha creado un data
- [x] Sismografo.py
- [x] TipoDeDato.py
- [x] Usuario.py

### Clases para las que no se ha creado un data
Para estas clases, si son necesarias en los atributos, se ha establecido como "None"

- [-] MagnitudRichter.py
- [-] ModeloSismografo.py
- [-] MotivoFueraServicio.py
- [-] OrigenDeGeneracion.py
- [-] Perfil.py
- [-] Reparacion.py
- [-] Rol.py
- [-] Suscripcion.py