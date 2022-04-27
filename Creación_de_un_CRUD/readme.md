# Creación de un CRUD con python

### Introducción
- [Básicos del lenguaje](#Introducción)
    - [Guia de instalación y conceptos básicos](#Qué_necesitas_saber_para_tomar_el_curso)
    - [IMPORTANTE: instalación Ubuntu Bash en windows para facilitarte el seguimiento del curso desde windows](#comó_organizar_las_carpetas_de_tus_proyectos)
    - [¿Qué es la programación?](#que_es_la_programacion)
    - [¿Por qué programar con Python?](#que_es_la_programacion)
    - [Operadores matemáticos](#que_es_la_programacion)
    - [Variables y expresiones](#que_es_la_programacion)
    - [Presentación del proyecto](#que_es_la_programacion)
    - [Funciones](#que_es_la_programacion)
    - [Usando funciones en nuestro proyecto](#que_es_la_programacion)
    - [Operadores lógicos](#que_es_la_programacion)
    - [Estructura condicionales](#que_es_la_programacion)
- [Static Typing](#Static_typing)
    - [¿Qué son los tipados?](#Qué_son_los_tipados)
    - [Tipado estático en python](#Tipado_estático_en_python)
    - [Practicando el tipado estático](#Practicando_el_tipado_estático)
- [Conceptos avanzados de funciones](#Linked_lists)
    - [Scope: alcance de las variables](#Nodos_y_singly_linked_list)
    - [Closures](#Crear_nodos)
    - [Programando closures](#Crear_singly_linked_lists)
    - [Decoradores](#Operaciones_en_single_linked_structures)
    - [Programando decoradores](#Operaciones_a_detalle)
- [Estructura de datos avanzadas](#Stacks)
    - [Iteradores](#Que_son_stacks)
    - [La sucesión de Fibonacci](#crear_stack)
    - [Generadores](#Que_son_stacks)
    - [Mejorando nuestra sucesión de Fibonacci](#crear_stack)
    - [sets](#Que_son_stacks)
    - [Operaciones con sets](#crear_stack)
    - [Eliminando los repetidos de una lista](#Que_son_stacks)
- [Bonus](#Queues)
    - [Manejo de fechas](#Que_son_los_queues)
    - [Time zones](#Queue_basada_en_listas)

# Básicos del lenguaje

### Guia de instalación y conceptos básicos

#### ¿Qué es Python?

Python es un lenguaje de programación creado por Guido Van Rossum, con una sintaxis muy limpia, ideado para enseñar a la gente a programar bien. Se trata de un lenguaje interpretado o de script.

#### Ventajas:

- **Legible:** sintaxis intuitiva y estricta.
- **Productivo:** ahorra mucho código.
- **Portable:** para todo sistema operativo.
- **Recargado:** viene con muchas librerías por defecto.

#### Instalación
Existen dos versiones de Python que tienen gran uso actualmente, Python 2.x y Python 3.x, para este curso necesitas usar una versión 3.x

Para instalar Python solo debes seguir los pasos dependiendo del sistema operativo que tengas instalado.

#### Windows
Para instalar Python en Windows ve al sitio https://www.python.org/downloads/ y presiona sobre el botón Download Python 3.7.3

Se descargará un archivo de instalación con el nombre python-3.7.3.exe , ejecútalo. Y sigue los pasos de instalación.

Al finalizar la instalación haz lo siguiente para corroborar una instalación correcta

- Presiona las teclas Windows + R para abrir la ventana de Ejecutar.
- Una vez abierta la ventana Ejecutar escribe el comando cmd y presiona ctrl+shift+enter para ejecutar una línea de comandos con permisos de administrador.
- Windows te preguntará si quieres abrir el Procesador de comandos de Windows con permisos de administrador, presiona sí.
- En la línea de comandos escribe py o python

Tu consola se mostrará así.

![src/version_py.PNG](src/version_py.PNG)

¡Ya estás listo para continuar con el curso!

#### MacOS

La forma sencilla es tener instalado homebrew y usar el comando:

**Para instalar la Versión 2.7**

`brew install python`

**Para instalar la Versión 3.x**

`brew install python3`

#### Linux

Generalmente Linux ya lo trae instalado, para comprobarlo puedes ejecutar en la terminal el comando

**Versión 2.7**

`python -v`

**Versión 3.x**

`python3 -v`

Si el comando arroja un error quiere decir que no lo tienes instalado, en ese caso los pasos para instalarlo cambian un poco de acuerdo con la distribución de linux que estés usando. Generalmente el gestor de paquetes de la distribución de Linux tiene el paquete de Python

Si eres usuario de Ubuntu o Debian por ejemplo puedes usar este comando para instalar la versión 3.1:

`$ sudo apt-get install python3.1`

Si eres usuario de Red Hat o Centos por ejemplo puedes usar este comando para instalar python

`$ sudo yum install python`

Si usas otra distribución o no has podido instalar python en tu sistema Linux dejame un comentario y vemos tu caso específico.

Si eres usuario habitual de linux también puedes descargar los archivos para instalarlo manualmente.

**Antes de empezar:**

Para usar Python debemos tener un editor de texto abierto y una terminal o cmd (línea de comandos en Windows) como administrador.

No le tengas miedo a la consola, la consola es tu amiga.

Para ejecutar Python abre la terminal y escribe:

`python`

Te abrirá una consola de Python, lo notarás porque el prompt cambia y ahora te muestra tres simbolos de mayor que “ >>> “ y el puntero adelante indicando que puedes empezar a ingresar comandos de python.

 `>>> `

En éste modo puedes usar todos los comandos de Python o escribir código directamente.

*Si deseas ejecutar código de un archivo sólo debes guardarlo con extension.py y luego ejecutar en la terminal:

` $ python archivo.py`

Ten en cuenta que para ejecutar el archivo con extensión “.py” debes estar ubicado en el directorio donde tienes guardado el archivo.

**Para salir de Python** y regresar a la terminal debes usar el comando exit()

Cuando usamos Python debemos atender ciertas reglas de la comunidad para definir su estructura. Las encuentras en el libro **PEP8**.

#### Tipos de datos en Python

- **Enteros (int):** en este grupo están todos los números, enteros y long:

ejemplo: 1, 2.3, 2121, 2192, -123

- **Booleanos (bool):** Son los valores falso o verdadero, compatibles con todas las operaciones booleanas ( and, not, or ):

 ejemplo: True, False

- **Cadenas (str):** Son una cadena de texto :

 ejemplos: “Hola”, “¿Cómo estas?”

- **Listas:** Son un grupo o array de datos, puede contener cualquiera de los datos anteriores:

 ejemplos: [1,2,3, ”hola” , [1,2,3] ], [1,“Hola”,True ]

- **Diccionarios:** Son un grupo de datos que se acceden a partir de una clave:

ejemplo: {“clave”:”valor”}, {“nombre”:”Fernando”}

- **Tuplas:** también son un grupo de datos igual que una lista con la diferencia que una tupla después de creada no se puede modificar.

ejemplos: (1,2,3, ”hola” , (1,2,3) ), (1,“Hola”,True ) 
(Pero jamás podremos cambiar los elementos dentro de esa Tupla)

En Python trabajas con módulos y ficheros que usas para importar las librerías.

#### Funciones

Las funciones las defines con **def** junto a un nombre y unos paréntesis que reciben los parámetros a usar. Terminas con dos puntos.

`def nombre_de_la_función(parametros):`

Después por indentación colocas los datos que se ejecutarán desde la función:

```python
 >>> def my_first_function():
 ...	return “Hello World!” 
 ...    
 >>> my_first_function()
    Hello World!
```

#### Variables

Las variables, a diferencia de los demás lenguajes de programación, no debes definirlas, ni tampoco su tipo de dato, ya que al momento de iterarlas se identificará su tipo. Recuerda que en Python todo es un objeto.

 ```python
 A = 3 
 B = A
 ```

#### Listas

Las listas las declaras con corchetes. Estas pueden tener una lista dentro o cualquier tipo de dato.

```python
 >>> L = [22, True, ”una lista”, [1, 2]] 
 >>> L[0] 
 22
 ```

#### Tuplas

Las tuplas se declaran con paréntesis, recuerda que no puedes editar los datos de una tupla después de que la has creado.

```python
 >>> T = (22, True, "una tupla", (1, 2)) 
 >>> T[0] 
 22
```

#### Diccionarios

**En los diccionarios tienes un grupo de datos con un formato:** la primera cadena o número será la clave para acceder al segundo dato, el segundo dato será el dato al cual accederás con la llave. Recuerda que los diccionarios son listas de llave:valor.

```python
 >>> D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"} 
 >>> D["Kill Bill"]
    "Tamarino"
```

#### Conversiones

- De flotante a entero:

```python
 >>> int(4.3)
 4
```

- De entero a flotante:

```python
 >>> float(4) 
 4.0
```

- De entero a string:

```python
 >>> str(4.3) 
 "4.3"
```

- De tupla a lista:

```python
 >>> list((4, 5, 2)) 
 [4, 5, 2]
```

#### Operadores Comunes

- Longitud de una cadena, lista, tupla, etc.:

```python
 >>> len("key") 
 3
```

- Tipo de dato:

```python
 >>> type(4) 
 < type int >
```

- Aplicar una conversión a un conjunto como una lista:

```python
 >>> map(str, [1, 2, 3, 4])
 ['1', '2', '3', '4']
```

- Redondear un flotante con x número de decimales:

```python
>>> round(6.3243, 1)
 6.3
```

- Generar un rango en una lista (esto es mágico):

```python
 >>> range(5) 
 [0, 1, 2, 3, 4]
```

- Sumar un conjunto:

```python
 >>> sum([1, 2, 4]) 
 7
```

- Organizar un conjunto:

```python
 >>> sorted([5, 2, 1]) 
 [1, 2, 5]
```

- Conocer los comandos que le puedes aplicar a x tipo de datos:

```python
 >>>Li = [5, 2, 1]
 >>>dir(Li)
 >>>['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

‘append’, ‘count’, ‘extend’, ‘index’, ‘insert’, ‘pop’, ‘remove’, ‘reverse’, ‘sort’ son posibles comandos que puedes aplicar a una lista.

#### Información sobre una función o librería:

```python
 >>> help(sorted) 
```

 (Aparecerá la documentación de la función sorted)

#### Clases

Clases es uno de los conceptos con más definiciones en la programación, pero en resumen sólo son la representación de un objeto. Para definir la clase usas_ class_ y el nombre. En caso de tener parámetros los pones entre paréntesis.

Para crear un constructor haces una función dentro de la clase con el nombre init y de parámetros self (significa su clase misma), nombre_r y edad_r:

```python
 >>> class Estudiante(object): 
 ... 	def __init__(self,nombre_r,edad_r): 
 ... 		self.nombre = nombre_r 
 ... 		self.edad = edad_r 
 ...
 ... 	def hola(self): 
 ... 		return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad) 
 ... 
 >>> e = Estudiante(“Arturo”, 21) 
 >>> print (e.hola())
 Mi nombre es Arturo y tengo 21
```
Lo que hicimos en las dos últimas líneas fue:

1. En la variable e llamamos la clase Estudiante y le pasamos la cadena “Arturo” y el entero 21.

2. Imprimimos la función hola() dentro de la variable e (a la que anteriormente habíamos pasado la clase).

Y por eso se imprime la cadena “Mi nombre es Arturo y tengo 21”

#### Métodos especiales

- cmp(self,otro)

Método llamado cuando utilizas los operadores de comparación para comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

- len(self)

Método llamado para comprobar la longitud del objeto. Lo usas, por ejemplo, cuando llamas la función len(obj) sobre nuestro código. Como es de suponer el método te debe devolver la longitud del objeto.

- init(self,otro)

Es un constructor de nuestra clase, es decir, es un “método especial” que se llama automáticamente cuando creas un objeto.

- Condicionales IF

Los condicionales tienen la siguiente estructura. Ten en cuenta que lo que contiene los paréntesis es la comparación que debe cumplir para que los elementos se cumplan.

```python
 if ( a > b ):
 	elementos 
 elif ( a == b ): 
 	elementos 
 else:
 	elementos
```

#### Bucle FOR

El bucle de for lo puedes usar de la siguiente forma: recorres una cadena o lista a la cual va a tomar el elemento en cuestión con la siguiente estructura:

```python
 for i in ____:
 	elementos
```

Ejemplo:

```python
 for i in range(10):
 	print i
```

En este caso recorrerá una lista de diez elementos, es decir el _print i _de ejecutar diez veces. Ahora i va a tomar cada valor de la lista, entonces este for imprimirá los números del 0 al 9 (recordar que en un range vas hasta el número puesto -1).

#### Bucle WHILE

En este caso while tiene una condición que determina hasta cuándo se ejecutará. O sea que dejará de ejecutarse en el momento en que la condición deje de ser cierta. La estructura de un while es la siguiente:

```python
 while (condición):
 	elementos
```

Ejemplo:

```python
 >>> x = 0 
 >>> while x < 10: 
 ... 	print x 
 ... 	x += 1
 ```

En este ejemplo preguntará si es menor que diez. Dado que es menor imprimirá x y luego sumará una unidad a x. Luego x es 1 y como sigue siendo menor a diez se seguirá ejecutando, y así sucesivamente hasta que x llegue a ser mayor o igual a 10.

Cómo seguir

No te preocupes si en este punto no entiendes algunos de estos conceptos, sigue con el curso donde vamos a realizar ejercicios que te ayuden a comprender y poder aplicar cada una de las características de Python.

Adelante!

### ¿Qué es la programación?

Es una disciplina que combina parte de otras disciplinas como las Matemáticas, Ingeniería y la Ciencia. Sin embargo, la habilidad más importante es resolver problemas. Es lo que harás todos los días como programador o programadora.

La programación es una secuencia de instrucciones que le damos a la computadora para que haga lo que nosotros deseamos. Podemos construir una aplicación web, móvil, un programa que lleve cohetes a la luna o marte, resolver problemas de finanzas.

La estructura de un programa. Casi todos los programas tienen un :
- input, 
- output, 
- operaciones matemáticas, 
- ejecución condicional y repeticiones

### ¿Por qué programar con Python?

Python es uno de los mejores lenguajes para principiantes porque tiene una sintaxis clara, una gran comunidad y esto hace que el lenguaje sea muy amigable para los que están iniciando.

Python esta diseñado para ser fácil de usar, a diferencia de otros lenguajes donde la prioridad es ser rápido y eficiente. Python no es de los lenguajes más rápidos, pero casi nunca importa.

Es el tercer lenguaje, según Github, entre los más populares. En StackOverflow se comenta que es uno de los lenguajes que mayor popularidad esta obteniendo.

““Python cuando podamos, C++ cuando necesitemos””

python --version para conocer la versión que tenemos instalada
python [nombre del archivo] para ejecutar nuestro programa

### Operadores matemáticos

En programación estos operadores son muy similares a nuestras clases básicas de matemáticas.

- //: Es división de entero, básicamente tiramos la parte decimal
- %: Es el residuo de la división, lo que te sobra.
- **: Exponente

```python
>>> 1+2    
3          
>>> 2-5    
-3         
>>> 10/4   
2.5        
>>> 10 // 4
2          
>>> 10 % 4 
2          
>>> 20 % 5 
0          
>>> 10 * 2 
20         
>>> 2 ** 8 
256        
>>> 'a' + 'b'
'ab'
>>> 'b' * 5
'bbbbb'       
```

Los operadores son contextuales, dependen del tipo de valor. Un valor es la representación de una entidad que puede ser manipulada por un programa.

Podemos conocer el tipo del valor con **type()** y nos devolverá algo similar a <class 'init'>, <class 'float'>, <class 'str'>. Dependiendo del tipo los operadores van a funcionar de manera diferente.

#### Operadores lógicos: 

Sirven para realizar comparaciones, devuelven un valor verdadero o falso.

| Operador	|Descripción				| Ejemplo|
| ----------- | ----------------------------  |------------- |
| and	      |¿se cumple a y b? 	          | r=True and False # r es False |
| or	      |¿se cumple a o b?	          | r=True o False # r es True |
| not	      | No a						  | r=not True #r es False |

#### Operadores relacionales: 

comparan dos expresiones y devuelven un valor verdadero o falso.

|Operador	    | Descripción 					|	Ejemplo|
| ------------- | ----------------------------  |------------- |
| == 			|	¿Son iguales a y b?			| r=5==3 # r es False|
| != 			|	¿Son distintos a y b?		| r=5!=3 # r es True |
| < 			|	¿Es a menor que b?			| r=5<3 # r es False |
| > 			|	¿Es a mayor que b?			| r=5>3 3 r es True  |
| <= 			|	¿Es a menor o igual que b?	| r=5<=5 # r es True |
| >= 			|	¿Es a mayor o igual que b?	| r=5>=3 # r es True |

### Variables y expresiones

Una variable es simplemente el contenedor de un valor. Es una forma de decirle a la computadora de que nos guarde un valor para luego usarlo.

Python es un lenguaje dinámico, este concepto de privado y público se genera por convenciones del lenguaje. En programación el signo = significa asignación.

Si una variable esta en mayúscula, usualmente se refiere a una constante, no debería reasignarse. Es una convención.

- message = 'How are you?'
- _age = 20 // variable privada
- PI = 3.14159
- __do_not_touch = 'something important' // variable que no debe modificarse

#### Reglas de Variables:

1. Pueden contener números y letras
2. No deben comenzar con número
3. Múltiples palabras se unen con _
4. No se pueden utilizar palabras reservadas

Expresiones son instrucciones para el interprete para evaluar la expresión. Los enunciados tienen efectos dentro del programa, como print que genera un output.

**orden de operaciones**

PEMDAS = Paréntesis, Exponente, Multiplicación-División, Adición-Sustracción

### Funciones

En el contexto de la programación las funciones son simplemente una agrupación de enunciados(statments) que tienen un nombre. Una función tiene un nombre, debe ser descriptivo, puede tener parámetros y puede regresar un valor después que se generó el cómputo.

Python es un lenguaje que se conoce como batteries include(baterías incluidas) esto significa que tiene una librería estándar con muchas funciones y librerías.

Para declarar funciones que no son las globales, las built-in functions, necesitamos importar un módulo.

Con el keyword **def** declaramos una función.

![src/funciones.PNG](src/funciones.PNG)

Otras funciones se pueden encontrar en módulos
- Para utilizarlas es necesario importar el módulo
    - Ejm: import math
- Para declarar una función, utilizamos el keyword **def**
    - Ej. def my_function(first_arg, second_arg=None)
- Las funciones se pueden componer.
    - Ej. def sum_two_numbers(x,y):
        return x + y

        other_function(sum_two_numbers(3,4))
- Los argumentos pueden ser posicionales o con nombre
    - Los parámetros y variables son locales a la función
        - global keyword
    - orden de ejecución:
        - Arriba para abajo
        - Izquierda a derecha

### Estructuras condicionales

- Una expresión booleana siempre se evalua como dos opciones verdadero (True) o como falso (False)
- Operadores de comparación
    - x = 2
    - y = 3
    - x == y
    - x != y
    - x > y
    - x < y
    - x >= y
    - x <= y

- Operadores logicos

- **and:** unicamente es verdadero cuando ambos valores son verdaderos

|X	    | Y 	 |	AND  |
| ------| ------ |------ |
| T 	|	T	 | T     |
| T 	|	F	 | F     |
| F 	|	T	 | F     |
| F 	|	F	 | F     |

- **or** es verdadero cuando uno de los dos valores es verdadero.

| X	    |   Y 	 |	OR  |
| ----- | ------ |----- |
| T 	|	T	 | T    |
| T 	|	F	 | T    |
| F 	|	T	 | T    |
| F 	|	F	 | F    |

- **not** es lo contrario al valor. Falso es Verdadero. Verdadero es Falso.

|X	    |  Y 	 |
| ------| ------ |
| T 	|	F	 |
| F 	|	T	 | 