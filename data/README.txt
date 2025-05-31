
- Punteros en Python

Explicacion de porque se hace uso de un diccionario en este proyecto:
    Su ausencia de punteros en python se debe a que el uso explícito de punteros es una característica de lenguajes de más bajo
    nivel como el C. Lenguajes de alto nivel como Python lo evitan con el propósito de hacer más fácil y ágil su utilización,
    así como no tener que conocer detalles del modelo de datos.

    Que el programador de Python no tenga que lidiar con los punteros no quiere decir que el intérprete no haga uso de ellos.
    De hecho los usa profusamente de forma implícita.

    En Python todo es un objeto creado en la memoria dinámica (mantenida automáticamente). Cuando llamas a una función los
    argumentos son pasados mediante sus punteros. Es lo que se conoce como convención de llamada por objeto. De igual forma
    si asignas a = b, a lo que guarda es el puntero del objeto de b. Así que todas las variables son punteros a objetos, que
    son manejados implícitamente.

    Lo que sí hay que diferenciar es entre objetos inmutables y mutables.

    Inmutables son los números, las cadenas o las tuplas. Al asignar x = 2015 creará un objeto entero y x apuntará a él pero el
    contenido de ese objeto no podrá ser modificado. Si luego asignas x = 2016 lo que hará internamente será crear un nuevo objeto
    con el nuevo contenido.
    Mutables son otros objetos como los diccionarios o las listas. En este caso dichos objetos sí podrán ser modificados. Si
    tienes v = [1] y luego llamas a v.append(2), v seguirá apuntando al mismo objeto, pero su contenido habrá cambiado.

- USO DEL DICCIONARIO

    NOMENCLARUTA para nombrar el archivo de diccionario
        El archivo que contiene el diccionario asociado a una clase debe nombrarse utilizando el siguiente formato:
        nombreClase_diccionario.py
        Ejemplo: eventoSismico_diccionario.py

    NOMENCLARUTA para nombrar el diccionario dentro del archivo
        El diccionario en sí debe nombrarse utilizando el siguiente formato:
        nombreClase_data
        Ejemplo: eventoSismico_data

    NOMENCLARUTA para nombrar los identificadores (nuestros punteros falsos)
        Cada registro tendrá un identificador generado a partir de las iniciales de la clase seguido de un número secuencial.
        Por ejemplo, para la clase EventoSismico, el identificador será la concatenación de las iniciales "ES" más un
        número creciente: "ES1", "ES2", ..., "ESn".
        
        En caso de que dos o más clases compartan las mismas iniciales, se agregarán letras adicionales del nombre de la clase
        hasta que los identificadores sean únicos.
        
        Por ejemplo, las clases Reparacion y Rol comienzan ambas con la letra "R", por lo que inicialmente sus identificadores
        serían "R1" para ambas. Para evitar esta duplicidad, se utilizan las siguientes letras del nombre de cada clase:
            Reparacion tendrá identificadores como "RE1", "RE2", ...
            Rol tendrá identificadores como "RO1", "RO2", ...
        
        De esta forma, se garantiza que cada identificador sea único y fácilmente asociable a su clase correspondiente.