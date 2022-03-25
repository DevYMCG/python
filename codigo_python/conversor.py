def resultado(valor_dolar, pesos):
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")

menu = """
Bienvenidos al conversor de monedas

1- Pesos Colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    resultado(3875, pesos)
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    resultado(65, pesos)
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    resultado(24, pesos)
else:
    print('Ingrese una opción correcta por favor')