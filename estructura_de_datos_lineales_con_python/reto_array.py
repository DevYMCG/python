"""
    1. crea una clase de array.
    2. Incorpora un método para poblar sus slots con números aleatorios o secuenciales
    3. Incluye un método que sume todos los valores del array.
"""
from functools import reduce
import random 

class Array:

    def __init__(self, capacity, fill_value=None):
        self.items = [random.randint(1,100) for i in range(capacity)]

    def __sumItems__(self):
        """returns the sum of all the values ​​in the array"""
        return reduce(lambda a, b: a+b, self.items)

    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)

if __name__ == "__main__":
    dimension = int(input('¿Ingresa la dimensión del array?: '))
    menu = Array(5)
    print(menu.__str__())
    print(menu.__sumItems__())