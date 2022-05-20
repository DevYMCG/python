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
