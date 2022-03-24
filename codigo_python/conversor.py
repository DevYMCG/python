menu = """
Bienvenidos al conversor de monedas

1- Pesos Colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 3875
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    valor_dolar = 65
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 24
    print("Tienes $"+ str(round(pesos / valor_dolar, 2)) + " dólares. ")
else:
    print('Ingrese una opción correcta por favor')