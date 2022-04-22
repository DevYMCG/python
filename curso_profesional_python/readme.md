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