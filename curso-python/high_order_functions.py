from functools import reduce
import math

def run():
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    
    # list_numeros_impares = [i for i in my_list if i%2!=0]

    # uso con filter

    # list_numeros_impares = list(filter(lambda x: x%2 != 0, my_list))


    # my_list = [1,2,3,4,5]

    # list = [i**2 for i in my_list] 

    # uso de map
    
    # squares = list(map(lambda x: x**2, my_list))

    #uso de reduces

    my_list = [2,2,2,2,2]
    # acum = 1

    # for value in my_list:
    #     acum= acum*value;

    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print(all_multiplied)


if __name__ == '__main__':
    run()