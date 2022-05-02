import random

def binary_search(data, target, low, high):
    """
        si el indice bajo es ma alto que el 
        indice final
    """
    if low > high:
        return False
    
    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()
    print(data)
    #sorted_data = sorted(data)
    """
        Regresa True si encontro el elemento
        False si no lo encontro.
        Parametros
        data = nuestros datos
        target = lo que queremos buscar
        0 = indice inicial
        len(data)-1 = indice final
    """
    target = int(input('What number would you like to find?'))
    found = binary_search(data, target, 0, len(data)-1)
    print(found)
