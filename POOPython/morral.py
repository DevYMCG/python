from unittest import result


def morral(tamano_morral, pesos, valores, n):
    
    """
        si nos quedan elementos y nos queda
        espacio en el morral
    """
    if n == 0 or tamano_morral == 0:
        return 0
    
    """
        si el elemento n-1 es mayor a el 
        tamaño del morral entonces debo revisar
        el proximo elemento.
    """
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)
    
    """
        tengo dos opciones: si decido tomar el elemento
        envio el tamaño del morral - el peso del elemento que tome
        lista de pesos, lista de valores y n-1
        y si no, envio el tamaño del morral , la lista de pesos, 
        valores y n-1
    """
    return max(valores[n-1] + morral(tamano_morral -pesos[n-1], pesos, valores, n-1), 
                morral(tamano_morral, pesos, valores, n-1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 5
    n = len(valores)

    result = morral(tamano_morral, pesos, valores, n)
    print(result)