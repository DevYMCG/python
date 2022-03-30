from dataclasses import replace
from operator import concat
import random

def imprimir(lista):
    for item in lista:
        print(item.upper(), end="")



def gano(lista, palabra):

    """
        Metodo que me permite comparar
        si los elementos que esta en la
        lista coinciden con los del
        string 'palabra'
    """

    lista_palabra = ""

    for letra in lista:
        lista_palabra = lista_palabra + letra
    
    lista_palabra = lista_palabra.replace(' ', '')

    if lista_palabra == palabra:
        return 0
    
    return 1



def adivina_palabra(palabra, lista):

    band = 1
    
    while band == 1:
        pedir_letra = input("\n Ingresa una letra: ")
        posicion = 0
        
        for letra in palabra:
            if letra.lower() == pedir_letra.lower():
                lista[posicion]=letra+" ";

            posicion+=1;  

        imprimir(lista)
        band = gano(lista, palabra)

    print("\n¡Ganaste! la palabra era", palabra)



def paint(palabra): 

    """
     metodo para pintar (-) segun la 
     longitud de la palabra
    """

    print("¡Adivina la palabra! " + palabra)
    # lista = []
    
    # for letra in range(0, len(palabra)):
    #     lista.append("_ ")
    lista = ["-" for letra in range(len(palabra))]

    imprimir(lista)
    adivina_palabra(palabra, lista)



def run():
    # palabras = []

    """
        leer del archivo data.txt las palabras
        que se encuentran y guardarlas en una
        lista
    """
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = [line for line in f]
        # for line in f:
        #     palabras.append(line)

    palabra_aleatoria = random.choice(palabras)
    palabra_aleatoria = palabra_aleatoria.replace('\n', '')
    paint(palabra_aleatoria)



if __name__ == '__main__':
    run()