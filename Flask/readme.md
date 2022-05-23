# Flask

Conoce todo el potencial de Flask como framework web de Python, integraciones con Bootstrap, GCloud, What The Forms y más.

Flask es sencillo de aprender, tiene una documentación clara y práctica, es rápido a la hora de renderizar puede ser hasta tres veces más rapido que Django. También es fácil de realizar una API REST, la estructura de un proyecto es flexible y es ideal para aprender desarrollo web con un framework de Python.

## ¿Cómo funcionan las aplicaciones en internet?

Cuando utilizas una aplicación web puedes interactuar con ella desde una computadora hasta un dispositivo móvil, pero esto no quiere decir que consume el procesamiento de tu dispositivo. Todo lo contrario, se hace en una red de servidores.

Estos servidores unen su poder de procesamiento con el fin transmitir solicitudes a todo el mundo, a su vez utilizar servidores especializados para almacenar los datos con los cuales se está trabajando, así como los datos de los demás usuarios. Como todo esto sucede sin demora alguna, parecerá que la aplicación se está ejecutando de forma nativa en tu dispositivo.

El servidor procesa la información obtenida por el navegador, luego se realizan los procedimientos necesarios de acuerdo a la lógica de negocio de la aplicación para regresar la información solicitada al cliente.

Ejemplo:

Cuando utilizamos Google Drive el cual es una aplicación web y abrimos un documento con Google Docs, el navegador se comunica con los servidores para ver y editar el documento.

A medida que vayas editando el documento, tu navegador trabajará de la mano con los servidores para asegurarse que todos los cambios se estén guardando.

Ventajas:

- Muchas de las aplicaciones web que existen son gratuitas.
- Puedes acceder a tu información en cualquier momento y lugar.
- No dependes de un dispositivo en específico ya que la aplicación se encuentra almacenada en la web.

## ¿Qué es Flask?

que es flask = es un microfamework, framework minimalista escrito en python es flexible es lo mas simple.

pip = librerias para manejar paquetes en pithon

## Instalación de Python, pip y virtualenv

Esta es la guía para configurar nuestro ambiente con Python 3.
Por lo general Mac ya incluye una instalación de Python, la puedes verificar ejecutando los siguientes comandos en una terminal:

```
python --version
python3 --version
```

Lanzamos el comando para crear el entorno virtual:

```
py -m venv env
```

Y después lo activamos:

```
# Windows
.\env\Scripts\activate
```

Para desactivar el modo virtual

```
deactivate
```

## Instalar Flask

Para instalar flask lo realizamo con el comando a continuación:

```
λ pip install flask
```

Comando para observar las dependencias instaladas.

```
pip freeze
```
Comando para sacar lo que hay en el virtualenv y agregarlo en el requirements tambien podemos usar esta linea:

```
pip freeze >> requirements.txt
```

## Creación de Hello word con Flask

Estos son los conceptos principales que debes entender antes de hacer un Hello World en Flask:

**virtualenv:** es una herramienta para crear entornos aislados de Python.

**pip:** es el instalador de paquetes para Python.

**requirements.txt:** es el archivo en donde se colocará todas las dependencias a instalar en nuestra aplicación.

**FLASK_APP:** es la variable para identificar el archivo donde se encuentra la aplicación.

creamos el archivo main.py

```python
from flask import Flask

app = Flask(__name__)

app.route('/')
def hello():
    return "Hello Word Flask"
```

Para correr nuestro servidor:

```
flask run
```
si nos devuelve este error:

>Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.

Entonces procedemos a realizar esto en la terminal:

```
set FLASK_APP=main.py
```
Luego ejecutamos el comando 

```
flask run
```
## Debugging en Flask

**Debugging:** es el proceso de identificar y corregir errores de programación.

Para activar el debug mode escribir lo siguiente en la consola:

```
set FLASK_DEBUG=1
```

**Logging:** es una grabación secuencial en un archivo o en una base de datos de todos los eventos que afectan a un proceso particular.

Se utiliza en muchos casos distintos, para guardar información sobre la actividad de sistemas variados.

Tal vez su uso más inmediato a nuestras actividades como desarrolladores web sería el logging de accesos al servidor web, que analizado da información del tráfico de nuestro sitio. Cualquier servidor web dispone de logs con los accesos, pero además, suelen disponer de otros logs, por ejemplo, de errores.

Los sistemas operativos también suelen trabajar con logs, por ejemplo para guardar incidencias, errores, accesos de usuarios, etc.

A través de el logs se puede encontrar información para detectar posibles problemas en caso de que no funcione algún sistema como debiera o se haya producido una incidencia de seguridad.

### Request y Response

Para usar el request tenemos que importarlo como se muestra en el codigo a continuación

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return 'Hello Word Platzi, tu IP es {}'.format(user_ip)
```

### Ciclos de Request y Response

**Request-Response:** es uno de los métodos básicos que usan las computadoras para comunicarse entre sí, en el que la primera computadora envía una solicitud de algunos datos y la segunda responde a la solicitud.

Por lo general, hay una serie de intercambios de este tipo hasta que se envía el mensaje completo.

**Por ejemplo:** navegar por una página web es un ejemplo de comunicación de request-response.

Request-response se puede ver como una llamada telefónica, en la que se llama a alguien y responde a la llamada; es decir hacemos una petición y recibimos una respuesta.

```python
from flask import Flask, redirect, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenemos la direccion ip del servidor
    user_ip = request.remote_addr 
    # redireccionamos al endpoint /hello
    response = make_response(redirect('/hello'))
    # Guardamos la ip en la cookie
    response.set_cookie('user_ip',user_ip)

    return response


@app.route('/hello')
def hello():
    # Obtenemos la ip de la cookie
    user_ip = request.cookies.get('user_ip')
    # retornamos la ip
    return 'Hello Word Platzi, tu IP es {}'.format(user_ip)
```
### Templates 

**Template :** Es un archivo HTML que nos permite renderizar información estatica y dinamica. 

Para renderizar un template se debe crear un archivo .html y llamarlo desde el main para esto hay que importar render_template.

```python
from flask import Flask, redirect, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenemos la direccion ip del servidor
    user_ip = request.remote_addr 
    # redireccionamos al endpoint /hello
    response = make_response(redirect('/hello'))
    # Guardamos la ip en la cookie
    response.set_cookie('user_ip',user_ip)

    return response


@app.route('/hello')
def hello():
    # Obtenemos la ip de la cookie
    user_ip = request.cookies.get('user_ip')
    # retornamos lo que haya en hello.html 
    return render_template('hello.html', user_ip=user_ip)
```

y en el archivo .html

```
<h1>Hello Word Platzi, tu IP es {{ user_ip }}</h1>
```

### Estructuras de control

Iteración: es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.

Un ejemplo de iteración sería el siguiente:

```python
{% for key, segment in segment_details.items() %}
        <tr>
                <td>{{ key }}td>
                <td>{{ segment }}td>
        tr>
{% endfor %}  
```

En este ejemplo estamos iterando por cada segment_details.items() para mostrar los campos en una tabla {{ key }} {{ segment }} de esta forma dependiendo de cuantos segment_details.items() haya se repetirá el código.

### Herencia de templates

Macro: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

```python
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% endif %}
{% endmacro %}
```

Un ejemplo de uso de macros en Flask:

```python
{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
<html>
```

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.

### Herencia de templates

**Macro:** son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

```html
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
    {% endif %}
{% endmacro %}
```

Un ejemplo de uso de macros en Flask:

```html
{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
html>
```

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.

### Include y Links

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}Flask Platzi | {% endblock %}
    </title>
</head>
<body>
    <header>
        {% include 'navbar.html' %}
    </header>
    {% block content %}
    {% endblock %}
</body>
</html>
```

