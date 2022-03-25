def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra_alreves= palabra[::-1]
    if palabra == palabra_alreves:
        return True

    return False 


def run():
    palabra = input("Ingrese la palabra para comprobar si es palindromo: ")
    es_palindromo = palindromo((palabra.lower()).strip())
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == '__main__':
    run()