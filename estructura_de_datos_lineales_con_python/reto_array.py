"""
    1. crea una clase de array.
    2. Incorpora un método para poblar sus slots con números aleatorios o secuenciales
    3. Incluye un método que sume todos los valores del array.
"""
import random 

class Array:

    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            numero_aleatorio = random.randint(1,100)
            self.items.append(numero_aleatorio)
    
    def __suma__(self):
        acum = 0
        for i in range(5):
            acum += self.items[i]
        
        return acum

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    dimension = int(input('¿Ingresa la dimensión del array?: '))
    menu = Array(5)
    print(menu.__str__())
    print(menu.__suma__())