import random


def run():
    numero_aleatorio = random.randint(1,100)
    numero = int(input("Elige un número del 1 al 100: "))

    while numero!=numero_aleatorio:

        if numero < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")

        numero = int(input("Elige otro número: "))

    print("¡Ganaste!")


if __name__ == "__main__":
    run()