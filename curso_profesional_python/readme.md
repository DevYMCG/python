# Curso Profesional d python

### Introducción
- [Introducción](#Introducción)
    - [¿Qué necesitas saber para tomar el curso?](#Qué_necesitas_saber_para_tomar_el_curso)
    - [¿Cómo funciona Python?](#Cómo_funciona_Python)
    - [¿Comó organizar las carpetas de tus proyectos?](#comó_organizar_las_carpetas_de_tus_proyectos)
- [Static Typing](#Static_typing)
    - [¿Qué son los tipados?](#Qué_son_los_tipados)
    - [Tipado estático en python](#Arrays_de_dos_dimensiones)
    - [Practicando el tipado estático](#Arrays_de_dos_dimensiones)
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

# Introducción

### ¿Qué necesitas saber para tomar el curso?

- Curso Basico de python
- Git / Github
- POO

### ¿Cómo funciona Python?

**Compilado vs Interpretado**

C++ es un lenguaje **compilado** por lo tanto lo que sucede en el motor de este lenguaje de programación es que el codigo se transforma mediante el compilador que es una herramienta que posee el lenguaje a código maquina es decir a 0 y 1 esto hace que la computadora pueda ejecutar el programa.

![src/compilado.PNG](src/compilado.PNG)

python por el contrario es un lenguaje **interpretado** al realizarse la conversión nosotros no pasamos a codigo máquina si no que pasamos a un estado intermedio con instrucciones que son legibles denominado byte code.

![src/interpretado.PNG](src/interpretado.PNG)

 El byte code es un lenguaje especial que es de mas bajo nivel que python que puede ser leido por un **interprete** la caracteristica especial es que este lenguaje es leido por una maquina virtual

![src/interpretado_vm.PNG](src/interpretado_vm.PNG)

La maquina virtual puede ser ejecutado en diferentes sistemas operativos.

**Definiciones**

**Garbage collector:** Tomar los objetos y las variables que no estan en uso y los elimina.

**__pycache__:** cuando se crea la carpeta __pycache__ lo que esta adentro de esta carpeta es byte code es ese codigo intermedio que crea python al ser un lenguaje interpretado para que pueda ser leido por la maquina virtual.

### ¿Comó organizar las carpetas de tus proyectos?

Para comprender como organizar los proyectos de python es importante tener en cuenta dos definiciones: paquetes y módulos

**Módulo:** un módulo es cualquier archivo de python. Generalmente, contiene código que puedes reutilizar.

**Paquete:** Un paquete es una carpeta que contiene módulos siempre  posee el archivo __init__.py

![src/paquete.PNG](src/paquete.PNG)

Ejemplo de organizar la estructura de un proyecto en python.

![src/estructura_de_carpetas.PNG](src/estructura_de_carpetas.PNG)

# Static Typing

### ¿Qué son los tipados?

Los tipados es una clasificación de los lenguajes de programación, tenemos cuatro tipos:

- Estático
- Dinámico
- Débil
- Fuerte

El tipado del lenguaje depende de cómo trata a los tipos de datos.

![src/tipos_tipado.PNG](src/tipos_tipado.PNG)

**estático**

El tipado estático es el que levanta un error en el tiempo de compilación, ejemplo en JAVA:

![src/tipado_static.PNG](src/tipado_static.PNG)

```java
String str = "Hello" // Variable tipo String
str = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.
```

**dinámico**

El tipado dinámico levantan el error en tiempo de ejecución, ejemplo en Python:

![src/tipado_dynamic.PNG](src/tipado_dynamic.PNG)

```python
str = "Hello" # Variable tipo String
str = 5 # La variable ahora es de tipo Entero, no hay error

## TIPADO FUERTE
x = 1
y = "2"
z = x + y # ERROR: no podemos hacer estas operaciones con tipos de datos distintos entre sí
```
**débil**

El tipado débil es el que hace un cambio en un tipo de dato para poder operar con el, como lo hace JavaScript y PHP.

```js
x = 1
y = "2"
z = x + y //12
```

```php
<?php
$str = 5 + "5" // equals 10 because "5" is implicity casted to 5 as an integer
// PHP is weakly typed, this is a very forgiving languaje
```

🐍 Python es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.

### Practicando el tipado estático

Como hacer para que el tipado de python de tipo dinámico sea estático **Static Typing**

 **Static Typing**

**Asignando el tipo a la variable**

 ```python
 a: int = 5
 print(a) // 5

 b: str = 'Hola'
 print(b) // Hola

 c: bool = True
 print(c) // True
 ```

 **Asignando el tipo a las funciones**

 ```python
def suma(a: int, b:int )->int:
    return a + b

print(suma(1,2)) // 3

def suma(a: int, b:int )->int:
    return a + b

print(suma('1','2')) // 12
 ```

![src/tipado_code.PNG](src/tipado_code.PNG)

En tipyng tenemos disponible la clase tupla

![src/tipado_tupla_dic.PNG](src/tipado_tupla_dic.PNG)

**mypy**

Es modulo especial en python que nos permite mostrar los errores en consola

**Ventaja de usar types**

- Aporta claridad y calidad al código va a ser mucho mas entendible
- Podremos visualizar errores antes de que el programa se ejecute.

**Crear nuestro entorno virtual**

 ```
py -m venv venv
 ```
**Entrar al entorno virtual**

 ```
 .\venv\Scripts\activate
 (venv) λ pip install mypy
  ```
 **Mejores prácticas usando tipo de variable**

 ```python
  def is_palindromo(String: str)->bool:
    String = String.replace(' ', '').lower()
    return String == String[::-1]

def run():
    print(is_palindromo(1000))


if __name__ == '__main__':
    run()

"""
(venv) λ mypy palindrome.py --check-untyped-defs
palindrome.py:6: error: Argument 1 to "is_palindromo" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
"""
 ```
 # Conceptos avanzados de funciones

 ### Scope: alcance de las variables

 Una variable solo está disponible dentro de la región donde fue creada.

**Local Scope**

Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

![src/local_scope.PNG](src/local_scope.PNG)

**Global Scope**

Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.

![src/global_scope.PNG](src/global_scope.PNG)

### Closures

Para entender los **clousures** tenemos que entender que son las funciones anidadas.

**Nested functions o (Funciones anidadas):** Son funciones que estan creadas dentro de otras funciones

![src/funciones_anidadas.PNG](src/funciones_anidadas.PNG)

un **clousure** es una variable que este en un scope superior y es recordada por una función que esta en un scope inferior. Aunque esta función sea eliminada anteriormente

![src/scope.PNG](src/scope.PNG)

```python
def main():
    
    a = 1

    def nested():
        print(a)

    return nested
    
my_func = main()
my_func()

del(main)

my_func()

```

**Reglas para encontrar un clousure**
- Debemos tener una nested función.
- La nested function debe referenciar un valor de un scope superior.
- La función debe retornarla también.

![src/scope_2.PNG](src/scope_2.PNG)

### Decoradores

Un **decorador** es un clousure su definión: Función que recibe como parámetro otra función, le añade cosas, y retorna una función diferente.

```python
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')

saludo();
# output
# ¡Hola!

saludo = decorador(saludo)
saludo()
#output
#Esto se añade a mi función original
# ¡Hola!
```

Esto se puede simplificar de la siguiente manera:

```python
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorador
def saludo():
    print('¡Hola!')

saludo()
#output
#Esto se añade a mi función original
#¡Hola!
```

# Estructura de datos avanzadas

### Iteradores

> Una estructura de datos para guardar datos infinitos.

Antes de entender qué son los iteradores, primero debemos entender a los iterables.

Son todos aquellos objetos que podemos recorrer en un ciclo. Son aquellas estructuras de datos divisibles en elementos únicos que yo puedo recorrer en un ciclo.

Pero en Python las cosas no son así. Los iterables se convierten en iteradores.

Ejemplo:

![src/iterador.PNG](src/iterador.PNG)

**¿Comó construir un iterador?**

![src/construir_iterador.PNG](src/construir_iterador.PNG)

**ventajas de usar iteradores**

- Un iterador nos ahorra recursos
- Ocupan poca memoria

El ciclo “for” dentro de Python, no existe. Es un while con StopIteration. 🤯🤯🤯

### La sucesión de Fibonacci

Ejemplo: 0 1 1 2 3 5 8 13 21 34 55 89 144 ....

```python
from itertools import count
import time

class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter()

    for n in fibonacci:
        print(n)
        time.sleep(1)

```

### Generadores

"Sugar syntax" de los iteradores.

- Los generadores son funciones a diferencia de los iteradores que son clases.

Nota: Yield es exactamente lo mismo que return la diferencia es que return para la función y retorna mientras yield pausa la función hasta donde estaba ese yiel

![src/generadores.PNG](src/generadores.PNG)

list comprehensions almacena todos los elementos en memoria por ejemplo:

![src/generadores_list.PNG](src/generadores_list.PNG)

**Ventajas de usar iteradores**

- Mas facil de escribir que un iterador.
- tienes la mismas ventajas que el iterador.

```python
import time

def Fibo_gen():

    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == "__main__":
    fiboGen = Fibo_gen()

    for n in fiboGen:
        print(n)
        time.sleep(1)

```

### sets

Una colección desordenada de elementos únicos e inmutables.

**¿Como crear un sets?**

![src/sets.PNG](src/sets.PNG)

**Como entiende python la declaración de sets**

![src/declaracion_sets.PNG](src/declaracion_sets.PNG)

**casting con los sets**

![src/catcs_sets.PNG](src/catcs_sets.PNG)

**Añadir elementos a un sets**

![src/anadir_elementos_sets.PNG](src/anadir_elementos_sets.PNG)

**diferencias entre discard y remove**

![src/quitar_elementos_sets.PNG](src/quitar_elementos_sets.PNG)

**Otra forma de borrar los elementos**

![src/borrar_elementos_sets.PNG](src/borrar_elementos_sets.PNG)

### Operaciones con sets

**Unión**

Resultado de combinar todos los elementos entre ambos

![src/union.PNG](src/union.PNG)

Ejemplo

![src/union_ejm.PNG](src/union_ejm.PNG)

**Intersección**

Resultado de combinar ambos sets pero quedarme solamente con los elementos que tienen en común

![src/interseccion.PNG](src/interseccion.PNG)

**ejemplo**

![src/interseccion_ejm.PNG](src/interseccion_ejm.PNG)

**Diferencias**

Es el resultado de tomar dos sets y de uno quitar todos los elementos que tiene el otro

![src/diferencia.PNG](src/diferencia.PNG)

**Ejemplo**

![src/diferencia_ejm.PNG](src/diferencia_ejm.PNG)

**Diferencia Simétrica**

Es lo contrario de la intercepción es el resultado de quedarme con los elementos de ambos sets pero sin los que se comparten

![src/diferencia_simetrica.PNG](src/diferencia_simetrica.PNG)

**ejemplo**

![src/diferencia_simetrica_ejm.PNG](src/diferencia_simetrica_ejm.PNG)




