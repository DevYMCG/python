# Parte 1: Cómo crear una API REST COMPLETA con FastAPI, instalación y estructura

## Que vamos a aprenderemos

En esta serie de tutoriales veremos como crear la estructura del proyecto, usar la autenticación con JWT, enrutamiento, conexiones a bases de datos y realizaremos tests para verificar el correcto funcionamiento de la aplicación.

## De que va el proyecto

El proyecto que vamos a realizar será una herramienta en la que podremos crear un usuario y este podrá tener un listado de tareas por hacer (también conocido como to-do list). Este podrá crearlas y después marcarlas como hechas

## Crear proyecto y entorno virtual e instalar FastAPI

Lanzamos el comando para crear el entorno virtual:

```python
python -m venv env
```
Y después lo activamos:

```python
# Windows
.\env\Scripts\activate
# Mac/linux
source env/bin/activate
```

Una vez hecho, instalaremos FastAPI y uvicorn que os explicaré a continuación que es y para qué lo utilizaremos:

```python
pip install fastapi uvicorn
```
Uvicorn es un servidor ASGI de alto rendimiento que usaremos para correr nuestra aplicación

Para ver nuestra API en funcionamiento, vamos a la terminal y lanzamos el siguiente comando:

```python
uvicorn main:app --reload
```

El comando uvicorn recibe un parámetro y una flag. El parámetro indica el nombre del archivo que queremos correr, después añadimos dos puntos y le indicamos el nombre de la variable que definimos como instancia de FastAPI.

El flag --reload hará que cada vez que ejecutemos un cambio en nuestro proyecto y guardemos, se recargue el proceso de uvicorn y se reflejen nuestros cambios en la API.

# Parte 2: Conexiones a bases de datos y creación de modelos con FastAPI

 En el tutorial de esta semana vamos a aprender cómo crear una conexión a nuestra base de datos PostgreSQL gracias a la librería peewee. También crearemos los modelos que nos permitirán generar nuestras tablas y que después utilizaremos también para poder realizar consultas a la base de datos.

Una vez instalado PostgreSQL, vamos a crear nuestra base de datos. Para ello accedéis a PostgreSQL y una vez dentro, lanzáis el siguiente comando que generará la base de datos:

```sql
 CREATE DATABASE to_do_list WITH OWNER = <your-database-user> ENCODING = 'UTF8' CONNECTION LIMIT = -1;
 ```
## Variables de entorno y settings

Ahora que tenemos la base de datos, ya podemos empezar a trabajar con ella desde nuestro proyecto. Para ello, primero vamos a guardar la información sobre la autenticación a la base de datos en el archivo .env que generamos en el tutorial anterior. Este archivo contendrá pares de clave-valor en el que deberéis reemplazar los valores de autenticación y conexión a la base de datos por los vuestros. Ejemplo:

# Database connection

```
DB_NAME=to_do_list
DB_USER=my-user
DB_PASS=my-pass
DB_HOST=localhost
DB_PORT=5432
```

El siguiente paso es instalar la librería python-dotenv que cargará automáticamente las variables de entorno que hemos generado en el archivo .env. Gracias a esto, podremos usarlas dentro de nuestro proyecto.

```
pip install python-dotenv
```

## Librería pydantic

Antes de seguir, vamos a explicar que es la librería pydantic, ya que en FastAPI la vamos a utilizar a menudo. Pydantic es una librería de Python la cual se encarga de realizar validaciones de datos, es decir que si por ejemplo creamos una clase extendiendo de una clase Base de pydantic y en ella declaramos una variable de tipo string (pydantic nos fuerza a asignar un tipo cada vez que declaramos una variable), si luego creamos una instancia de esta clase e intentamos asignar un valor de tipo booleano a esa variable, esta lanzará una excepción indiciando que el tipo de dato es erróneo.

Una vez explicado esto seguimos. Ahora vamos a emplear la clase BaseSettings de pydantic. Esta clase la emplearemos para guardar la configuración de nuestro proyecto como por ejemplo las variables de entorno que creamos hace un momento.

Para ello, vamos al directorio /app/v1/utils y dentro de él, generamos un archivo llamado settings.py que contendrá el siguiente código:

```python
import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
```

Primero importamos las librerías que necesitaremos, en este caso os para poder leer las variables de entorno, la clase BaseSettings y la función load_dotenv de la librería python-dotenv la cual se encargará de leer las variables de entorno.

Después declaramos la clase Settings que extenderá de BaseSettings y para finalizar declaramos las variables que guardarán la información sobre la conexión y autenticación a la base de datos.

Los valores los asignamos gracias a la función getenv de la librería os la cual recibe el nombre que les dimos a las variables de entorno en el archivo .env y si existen retornan su valor. Si no es así, devolverá None.

### Conexión a la base de datos

Ahora que ya podemos leer las variables de entorno, es hora de conectarnos a la base de datos. Para ello primero vamos a instalar peewee, ya que será el ORM que vamos a utilizar en este proyecto y psycopg2 que es la librería que hace de puente entre PostgreSQL y Python:

```
pip install psycopg2
pip install peewee
```

Una vez instaladas las librerías nos dirigimos de nuevo al directorio /app/v1/utils y generamos un archivo llamado db.py, este contendrá el siguiente código:

```python
import peewee
from contextvars import ContextVar
from fastapi import Depends

from app.v1.utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port


db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

db._state = PeeweeConnectionState()

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
```

Este archivo básicamente es una copia del tutorial de FastAPI para realizar la conexión con peewee. Lo que estamos haciendo primero es crear una instancia de clase Settings que creamos unos pasos más atrás y después guardar las variables de entorno de la conexión en constantes.

Posteriormente, sobreescribimos la clase PeeweeConnectionState, esto se hace por el asincronismo y está mejor explicado en el tutorial de FastAPI que os he dejado en el párrafo anterior.

El siguiente paso es efectuar la conexión a la base de datos de PostgreSQL, aquí es donde empleamos los parámetros de autenticación y conexión.

Por último, las funciones reset_db_state y get_db las utilizaremos para poder utilizar la conexión a la base de datos en todo nuestro proyecto. También podéis encontrar más información acerca de estas funciones en el tutorial de FastAPI que os dejé antes.

## Creación de modelos

Ahora que ya tenemos la conexión a la base de datos es hora de crear los modelos de peewee, estos los usaremos para nuestras tablas en la base de datos y también para poder realizar consultas, insertar datos, actualizarlos, etc.

Nuestra base de datos constará de dos tablas, una para almacenar los usuarios llamada user y otra tabla llamada todo que almacenará las tareas hechas y por hacer de un usuario.

El primer modelo que vamos a crear será el de usuarios. Para ello vamos al directorio /app/v1/model y creamos un archivo llamado user_model.py:

```python
import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    class Meta:
        database = db
```

Esta clase extiende de peewee.Model y en ella declaramos los campos que vamos a necesitar que será un email, username y password. El id no es necesario definirlo, ya que peewee se encargará de crearlo automáticamente como clave primaria y autoincrement.

Después añadimos la clase Meta dentro de la clase User que contendrá la conexión a la base de datos.

Si queréis más información acerca de que tipos de datos podéis crear con peewe os dejo el enlace a su documentación.

El siguiente modelo es el modelo todo. Para ello en la misma carpeta creamos un archivo llamado todo_model.py con el siguiente contenido:

```python
from datetime import datetime

import peewee

from app.v1.utils.db import db
from .user_model import User


class Todo(peewee.Model):
    title = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now)
    is_done = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="todos")

    class Meta:
        database = db
```

En este caso tendremos cuatro columnas (más el id que se genera automáticamente). El campo title será una breve descripción de la tarea a realizar, created_at será la fecha de creación, un booleano llamado is_done para indicar si la tarea ya ha sido realizada o no que por defecto se guardará como false y una clave foránea user para indicar a que usuario corresponde el todo. Esto guardará en la base de datos como un campo llamado user_id.

Por último, vamos a generar un script que se encargará de crear las tablas. Para ello vamos al directorio /app/v1/scripts y dentro creamos un archivo llamado create_tables.py con el siguiente contenido:

```python
from app.v1.model.user_model import User
from app.v1.model.todo_model import Todo

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Todo])
```

En este archivo importamos los modelos User y Todo además del objeto de la base de datos y después definimos una función que se conectará a la base de datos, recibirá una lista de los modelos que queremos convertir en tablas y después cerrará la conexión.

Para ejecutar este script, en la terminal vamos al directorio raíz de nuestro proyecto y escribimos py o python para acceder a la terminal de Python y poder ejecutar código en este lenguaje.

Una vez dentro de la terminal, escribimos la siguiente línea para importar la función que acabamos de crear y pulsamos enter:

```python
from app.v1.scripts.create_tables import create_tables
```

Una vez importada nuestra función solo debemos ejecutarla, para ello escribimos el nombre de la función más paréntesis y pulsamos enter (ejecutar una función de toda la vida vamos):

```python
create_tables()
```

Listo, si todo ha ido bien ya deberíamos tener creadas nuestras tablas en la base de datos.