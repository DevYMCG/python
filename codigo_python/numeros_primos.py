def run():
    numero = int(input('Escribe un número para conocer los primos que existan en este rango: '))
    for i in range(numero):
        contador = 1
        cont=0

        while(contador < numero):
            if i%contador==0:
                cont+=1

            contador+=1
        
        if(cont==2):
            print("El número: "+str(i)+" es primo")
            


if __name__ == '__main__':
    run()