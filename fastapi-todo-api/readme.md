# Que vamos a aprenderemos

En esta serie de tutoriales veremos como crear la estructura del proyecto, usar la autenticación con JWT, enrutamiento, conexiones a bases de datos y realizaremos tests para verificar el correcto funcionamiento de la aplicación.

# De que va el proyecto

El proyecto que vamos a realizar será una herramienta en la que podremos crear un usuario y este podrá tener un listado de tareas por hacer (también conocido como to-do list). Este podrá crearlas y después marcarlas como hechas

# Crear proyecto y entorno virtual e instalar FastAPI

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