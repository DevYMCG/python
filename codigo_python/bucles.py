def run(exponente):
    if exponente < 1000:
        print("2^"+str(exponente)+" = "+str(2**exponente))
        run(exponente+1)
    else:
        print("Fin!!")


if __name__ == '__main__':
    run(1)