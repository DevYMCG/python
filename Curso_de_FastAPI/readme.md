# Curso de FastAPI: Fundamentos, Path Operations y Validaciones

## ¿Qué es FastAPI?

El framework mas veloz para el desarrollo web con Python. Enfocado para realizar APIs, es el mas rápido en lo que respecta a la velocidad del servidor superando a Node.Js y a GO. Fue creado por Sebastian Ramirez, es de código abierto y se encuentra en Github, es usado por empresas como Uber, Windows, Netflix y Office.

## Ubicación de FastAPI en el ecosistema de Python

FastAPI utiliza otros frameworks dentro de si para funcionar

- Uvicorn: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor
- Starlette: es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente
- Pydantic: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API

## Hello World: creación del entorno de desarrollo

### crear entorno virtual

```
$ py -m venv venv
```

### Activar entorno virtual

```
λ .\venv\Scripts\activate
```

### Instalar fastAPI

```
λ pip install fastapi uvicorn
```

### creando nuestra primer path

```python
from fastapi import FastAPI

app = FastAPI()

# path de la ruta
@app.get("/")
def home():
    return {"Hello": "world"}
```

#### Para correr nuestro función.

(venv) λ uvicorn main:app --reload

Al ejecutar el comando nos va a aparecer el servidor corriendo como en la imagen adjunta.

![src/correr_app.PNG](src/correr_app.PNG)

Nos dirigimos al servidor y a continuación observamos lo que nos retorna la ruta que estamos consultando.

![src/api_main.PNG](src/api_main.PNG)

#### Documentación interactiva de una API

FastAPI también está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs. Es un conjunto de reglas que permiten decir que una API está bien definida.
ㅤ
OpenAPI necesita de un software, el cual es **Swagger**, que es un conjunto de softwares que permiten trabajar con APIs. FastAPI funciona sobre un programa de Swagger el cual es Swagger UI, que permite mostrar la API documentada.
ㅤ
Acceder a la documentación interactiva con Swagger UI:

```
{localhost}/docs
http://127.0.0.1:8000/docs
```

![src/docs.PNG](src/docs.PNG)

Acceder a la documentación interactiva con Redoc:

```
{localhost}/redoc
http://127.0.0.1:8000/redoc
```

![src/redoc.PNG](src/redoc.PNG)