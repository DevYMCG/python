from re import A
import time

def Fibo_gen(max : int):

    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux > max:
                return StopIteration
            n1, n2 = n2, aux
            counter += 1
            yield aux
        # else:
        #     return StopIteration

if __name__ == "__main__":
    max = int(input('Ingresa un número limite para la serie de fibonacci: '))
    fiboGen = Fibo_gen(max)

    for n in fiboGen:
        print(n)
        time.sleep(1)