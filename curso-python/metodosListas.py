def run():
    lista = [1,2,3,4,5]

    #Añadir un item al final de la lista
    lista.append(6)
    print(lista)

    # vaciar todos los items de una lista
    lista.clear()
    print(lista)

    # Une una lista a otra
    l1 = [1,2,3]
    l2 = [4,5,6]
    l1.extend(l2)
    print(l1)

    #cuenta el número de veces que aparece un ítem
    print(["Hola", "mundo", "mundo"].count("mundo"))

    #Devuelve el índice en el que aparece un ítem (error si no aparece)
    print(f'indice: {["Hola", "mundo", "mundo"].index("mundo")}')

    #Agrega un ítem a la lista en un índice específico:
    l = [1,2,3]
    l.insert(0,0)
    l.insert(0,-1)
    print(l)

    #Penultima posición (-1):
    l = [5,10,15,25]
    l.insert(-1,20)
    print(l)

    # Última posición en una lista con len():
    l = [5,10,15,25]
    n = len(l)
    l.insert(n,30)
    print(l)

    #Extrae un ítem de la lista y lo borra:
    l = [10,20,30,40,50]
    print(l.pop())
    print(l)

    #Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):
    print(l.pop(0))
    print(l)

    #Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
    l = [20,30,30,30,40]
    l.remove(30)
    print(l)

    #Le da la vuelta a la lista actual:
    l.reverse()
    print(l)

    #Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:
    lista = list("Hola mundo")
    lista.reverse()
    cadena = "".join(lista)
    print(cadena)

    #Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
    lista = [5,-10,35,0,-65,100]
    lista.sort()
    print(lista)

    #Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:
    lista.sort(reverse=True)
    print(lista)

if __name__ == '__main__':
   run()