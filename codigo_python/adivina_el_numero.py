import random


def buscar_numero(numero, rand):
    print("elegido "+str(rand))

    while numero != rand:
        if(numero < rand):
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
            
        numero = int(input("Elige un número del 1 al 100: "))

    print("¡Ganaste!")


def run():
    rand = random.randint(1,100)
    numero = int(input("Elige un número del 1 al 100: "))
    buscar_numero(numero, rand)


if __name__ == "__main__":
    run()