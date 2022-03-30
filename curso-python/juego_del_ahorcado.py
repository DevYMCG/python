from operator import concat
import random

def imprimir(lista):
    for item in lista:
        print(item, end="")



def gano(lista, palabra):
    palabras = ""
    palabra = palabra.replace('\n', '')

    for letra in lista:
        palabras = palabras + letra
    
    palabras = palabras.replace(' ', '')

    if palabras == palabra:
        return 0
    
    return 1



def adivina_palabra(palabra, lista):

    ganar = 1
    
    while ganar == 1:
        pedir_letra = input("\n Ingresa una letra: ")
        posicion = 0
        
        for letra in palabra:
            if letra == pedir_letra:
                lista[posicion]=letra+" ";

            posicion+=1;  

        imprimir(lista)
        ganar = gano(lista, palabra)

    print("\n¡Ganaste! la palabra era", palabra)



def paint(palabra): 
    print("¡Adivina la palabra! " + palabra)
    lista = []
    for letra in range(1, len(palabra)):
        lista.append("_ ")
    
    imprimir(lista)
    adivina_palabra(palabra, lista)



def run():
    data = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)

    palabra_aleatoria = random.choice(data)
    print(" palabra = "+palabra_aleatoria)
    paint(palabra_aleatoria)



if __name__ == '__main__':
    run()