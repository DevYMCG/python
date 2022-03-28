from unicodedata import numeric


def run():
    # list = []

    # for numero in range(1,101):
    #     if numero%3!=0:
    #         list.append(numero**2)
    
    list = [i**2 for i in range(1, 101) if i%3!=0]
    print(list)



if __name__ == '__main__':
    run()