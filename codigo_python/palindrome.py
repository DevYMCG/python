def palindrome(nombre):
    nombre = nombre.replace(' ', '')
    alreves= nombre[::-1]
    if nombre == alreves:
        return True

    return False 


def run():
    palabra = input("Ingrese la palabra para comprobar si es palindrome: ")
    es_palindromo = palindrome((palabra.lower()).strip())
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()