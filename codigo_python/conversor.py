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