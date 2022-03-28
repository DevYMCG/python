from unicodedata import numeric


def run():
    # list = []

    # for numero in range(1,101):
    #     if numero%3!=0:
    #         list.append(numero**2)
    
    # list = [i**2 for i in range(1, 101) if i%3!=0]

    """
       Crear una lista de todos los 
       multiplos de 4 que a la vez tambien
       sean multiplos de de 6 y 9 
    """

    # list = [i for i in range(1, 10000) if i%4==0 and i%6==0 and i%9==0]
    list = [i for i in range(1, 10000) if i%36==0]
    print(list)



if __name__ == '__main__':
    run()