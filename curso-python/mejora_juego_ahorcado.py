from dataclasses import replace
from operator import concat
import random
import os

def imprimir(lista):
    for item in lista:
        print(item.upper(), end="")



def gano(lista, palabra):

    cont = 0

    for index, letra in enumerate(palabra):
        palabra_lista = lista[index] .replace(' ', '')
        if palabra_lista == palabra[index]:
            cont+= 1

    if len(palabra)== cont:
        return 0
    
    return 1


def adivina_palabra(palabra, lista):

    band = 1
    
    while band == 1:
        os.system ("cls")
        pedir_letra = input("\n Ingresa una letra: ")
        
        for index, letra in enumerate(palabra):
            if palabra[index].lower() == pedir_letra.lower():
                lista[index]=letra+" ";

        imprimir(lista)
        band = gano(lista, palabra)

    os.system ("cls")
    print("\n¡Ganaste! la palabra era", palabra)



def paint(palabra): 

    print("¡Adivina la palabra! " + palabra)

    lista = ["_ " for letra in range(len(palabra))]

    imprimir(lista)
    adivina_palabra(palabra, lista)



def run():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = [line for line in f]

    palabra_aleatoria = random.choice(palabras)
    palabra_aleatoria = palabra_aleatoria.replace('\n', '')
    paint(palabra_aleatoria)



if __name__ == '__main__':
    run()