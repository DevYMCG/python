def divisors(num):
    divisors = []
    try:
        if num < 1:
            raise ValueError("No debes ingresar números negativos")
        for i in range(1, num +1):
            if num%i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return False



def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un números")



if __name__ == '__main__':
    run()