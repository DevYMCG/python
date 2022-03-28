import math

def run():
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    
    # list_numeros_impares = [i for i in my_list if i%2!=0]

    # uso con filter

    # list_numeros_impares = list(filter(lambda x: x%2 != 0, my_list))


    my_list = [1,2,3,4,5]

    # list = [i**2 for i in my_list] 

    # uso de map
    
    squares = list(map(lambda x: x**2, my_list))

    print(squares)


if __name__ == '__main__':
    run()