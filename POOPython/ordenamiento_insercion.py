import random

def ordenamiento_por_insersion(lista):

    n = len(lista) # 
    sublista= []

    for i in range(n-1):
        if lista[i+1] < lista[i]: 
            lista[i+1], lista[i] = lista[i], lista[i+1]
            if lista[i] < lista[i-1]:
                for k in range(i, -1, -1):
                    if lista[k] < lista[k-1]:
                        lista[k-1], lista[k] = lista[k], lista[k-1]
                    
                    if(k==1):
                        break
                        

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for  i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insersion(lista)
    print(lista_ordenada)