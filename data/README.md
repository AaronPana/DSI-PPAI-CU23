# DICCIONARIO
## Nomenclatura

### Nombrar el archivo de diccionario
El archivo que contiene el diccionario asociado a una clase debe nombrarse utilizando el siguiente formato: nombreClase_diccionario.py

Ejemplo: eventoSismico_diccionario.py

### Nombrar el diccionario

El diccionario en sí debe nombrarse utilizando el siguiente formato: nombreClase_data

Ejemplo: eventoSismico_data

### Nombrar los identificadores (nuestros punteros falsos)
        
Cada registro tendrá un identificador generado a partir de las iniciales de la clase seguido de un número secuencial. Por ejemplo, para la clase EventoSismico, el identificador será el nombre de la clase en PascalCase más un número creciente: NombreClaseN 

Ejemplo: "AlcanceSismo1", "AlcanceSismo2", ..., "AlcanceSismoN".

### Datos de atributos

Cuando un atributo tipo nombre representa un valor constante que no debe modificarse, **del cual se debe ralizar una comparacion en codigo** —como el nombre de un estado, un tipo o una categoría fija— debe escribirse en mayúsculas, utilizando guiones bajos para separar palabras.

Ejemplo: "nombre": "SISMOS_LOCALES"

---

## Punteros en Python
### Explicacion de porque se hace uso de un diccionario en este proyecto:
    
Su ausencia de punteros en python se debe a que el uso explícito de punteros es una característica de lenguajes de más bajo nivel como el C. Lenguajes de alto nivel como Python lo evitan con el propósito de hacer más fácil y ágil su utilización, así como no tener que conocer detalles del modelo de datos.

Que el programador de Python no tenga que lidiar con los punteros no quiere decir que el intérprete no haga uso de ellos. De hecho los usa profusamente de forma implícita.

En Python todo es un objeto creado en la memoria dinámica (mantenida automáticamente). Cuando llamas a una función los argumentos son pasados mediante sus punteros. Es lo que se conoce como convención de llamada por objeto. De igual forma si asignas a = b, a lo que guarda es el puntero del objeto de b. Así que todas las variables son punteros a objetos, que son manejados implícitamente.

Lo que sí hay que diferenciar es entre objetos inmutables y mutables.

Inmutables son los números, las cadenas o las tuplas. Al asignar x = 2015 creará un objeto entero y x apuntará a él pero el contenido de ese objeto no podrá ser modificado. Si luego asignas x = 2016 lo que hará internamente será crear un nuevo objeto con el nuevo contenido. Mutables son otros objetos como los diccionarios o las listas. En este caso dichos objetos sí podrán ser modificados. Si tienes v = [1] y luego llamas a v.append(2), v seguirá apuntando al mismo objeto, pero su contenido habrá cambiado.

---

# Data

- [x] AlcanceSismo.py
- [ ] CambioEstado.py
- [x] ClasificacionSismo.py
- [x] DetalleMuestraSismica.py
- [x] Empleado.py
- [x] EstacionSismologica.py
- [x] Estado.py
- [x] EventoSismico.py
- [-] MagnitudRichter.py
- [-] ModeloSismografo.py
- [-] MotivoFueraServicio.py
- [x] MuestraSismica.py
- [ ] OrigenDeGeneracion.py
- [-] Perfil.py
- [-] Reparacion.py
- [-] Rol.py
- [x] SerieTemporal.py
- [ ] Sesion.py
- [x] Sismografo.py
- [-] Suscripcion.py
- [x] TipoDeDato.py
- [x] Usuario.py