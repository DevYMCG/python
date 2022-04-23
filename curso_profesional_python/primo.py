def is_primo(numero: int)->bool:
    contador = 1
    cont = 0

    while(contador <= numero):
        if numero%contador==0:
            cont+=1
        contador +=1

    return cont==2  

def run():
    print(is_primo(17))


if __name__ == '__main__':
    run()