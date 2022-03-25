import random


def buscar_numero():
    rand = random.randint(1,100)
    numero = int(input("Elige un número del 1 al 100: "))

    while True:

        if numero == rand:
            break
        elif(numero < rand):
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")

        numero = int(input("Elige otro número: "))

    print("¡Ganaste!")


def run():
    buscar_numero()


if __name__ == "__main__":
    run()