import random


def buscar_numero():
    numero_aleatorio = random.randint(1,100)
    numero = int(input("Elige un número del 1 al 100: "))

    while True:

        if numero == numero_aleatorio:
            break
        elif(numero < numero_aleatorio):
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")

        numero = int(input("Elige otro número: "))

    print("¡Ganaste!")


def run():
    buscar_numero()


if __name__ == "__main__":
    run()