def palindrome(string):
    try:
        if len(string)==0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

    """
        Error al enviar un número.
        input  : palindrome(1)
        autput : TypeError: 'int' object is not subscriptable
    """
try:
    print(palindrome(""))
except TypeError:
    print("Solo se puede ingresar string")