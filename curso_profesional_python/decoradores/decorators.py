from datetime import datetime

"""
    Cuanto tiempo tarda en ejecutarse una 
    función para esto importamos el modulo 
    datetime
"""

def execution_time(func):
    """
    *args, **kwargs
    no importa la cantidad de argumentos posicionales que 
    se le envien la función los va a recibir,
    no importa la cantidad de argumentos nombrados que 
    se le envien la función los va a recibir
    """
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("pasaron"+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    # el _ indica que nos nos interesa saber la variable en cada una de las vueltas
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a:int , b:int)->int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola "+ nombre)

random_func()
suma(1,2)
saludo("Yoha")