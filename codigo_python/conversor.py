def resultado(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos "+ tipo_pesos+" tienes?: "))
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")

menu = """
Bienvenidos al conversor de monedas

1- Pesos Colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    resultado("pesos colombianos",3875)
elif opcion == 2:
    resultado("pesos argentinos",65)
elif opcion == 3:
    resultado("pesos mexicanos",24)
else:
    print('Ingrese una opción correcta por favor')