import math

def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i%3!=0}

    """
        Crear, un dictionary comprehension, un 
        diccionario cuyas llaves sean los 1000
        primeros números naturales con sus raíces
        cuadradas como valores
    """

    my_dict = {i: round(math.sqrt(i),2) for i in range(1, 1001)}
    
    print(my_dict)


if __name__ == '__main__':
    run()