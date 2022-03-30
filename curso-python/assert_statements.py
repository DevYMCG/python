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
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")



if __name__ == '__main__':
    run()