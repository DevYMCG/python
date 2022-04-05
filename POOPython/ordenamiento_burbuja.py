import random

def ordenamiento_burbuja(lista):
    band = False

    while(band==False):
        n = 0
        orden = 0
        while(n != (len(lista)-1)): 
            if(lista[n] > lista[n+1]):
                numero = lista[n]
                lista[n] = lista[n+1]
                lista[n+1] = numero
                n+=1
            else:
                n+=1
                orden+=1

        if(orden == ((len(lista)-1))):
            band = True
    
    print(f' orden = {lista}')

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for  i in range(tamano_de_lista)]
    print(lista)

    encontrado = ordenamiento_burbuja(lista)