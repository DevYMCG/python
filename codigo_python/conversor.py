pesos = input("¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $"+ dolares + " dólares")

dolares = input("¿cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso_colombiano = 3875
pesos = dolares*valor_peso_colombiano
print("Tienes COP "+ str(pesos))