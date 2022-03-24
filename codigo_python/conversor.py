pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
print("Tienes $"+ str(round(dolares, 2)) + " dólares")

dolares = input("¿Cuántos dolares tienes?: ")
dolares = float(dolares)
valor_peso_colombiano = 3875
pesos = dolares*valor_peso_colombiano
print("Tienes COP "+ str(pesos)+ " colombianos")

opcion = input("¿Deseas: opc1: Pesos-Dolares opc2: Dolares-pesos? (Responde 1 o 2) ")
if opcion == "opc1":
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3.800
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")
elif opcion == "opc2":
    dolares = float(input("¿Cuántos dolares tienes?: "))
    valor_peso = 3.800
    print("Tienes COP"+ str(round(dolares / valor_peso, 2)) + " pesos. ")