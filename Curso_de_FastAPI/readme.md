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

### Path Operations

¿Cómo funcionan las PATH OPERATION?

![src/path_operation.PNG](src/path_operation.PNG)

¿Que es un path?
Un path es lo mismo que un route o endpoints y es todo aquello que vaya después de nuestro dominio a la derecha del mismo.

¿Que son las operations?
Un operations es exactamente lo mismo que un método http y tenemos las siguientes más populares: GET, POST, PUT y DELETE

Y otros métodos como OPTIONS, HEAD, PATCH …

### Path Parameters

https://fastapi.tiangolo.com/tutorial/path-params/

Los parámetros de ruta son partes variables de una ruta URL . Por lo general, se utilizan para señalar un recurso específico dentro de una colección, como un usuario identificado por ID. Una URL puede tener varios parámetros de ruta.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

![src/path_parameters.PNG](src/path_parameters.PNG)

### Query Parameters

https://fastapi.tiangolo.com/tutorial/query-params/

Query parameters: son un conjunto definido de parámetros adjuntos al final de una URL . Son extensiones de la URL que se utilizan para ayudar a definir contenido o acciones específicos en función de los datos que se transmiten.

![src/parameters_opcionales.PNG](src/parameters_opcionales.PNG)

### Request Body y Response Body

Documentacion: https://fastapi.tiangolo.com/tutorial/body/

Un Request Body son datos enviados por el cliente a su API.

Un Response Body son los datos que su API envía al cliente.

![src/request_body.PNG](src/request_body.PNG)

### Models

Documentacion Oficial: https://fastapi.tiangolo.com/tutorial/sql-databases/

Un modelo es la representacion de una entidad en codigo, al menos de una manera descriptiva.

¿Como luce un modelo dentro de FastAPI?

Modelo pydantic para validar datos:

```python
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
```

Un modelo para mapear los datos a la base de datos (ORM, SQLalchemy)

```python
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
```

### Validaciones: Query Parameters

```python
#Python
from typing import Optional

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: str = Query(...)
): 
    return {name: age}
```