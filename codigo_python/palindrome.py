from operator import truediv
from pickle import TRUE

def palindrome(nombre):
    band= False
    alreves= nombre[::-1]
    if nombre == alreves:
        band= True

    return band 

palabra = input("Ingrese la palabra para comprobar si es palindrome: ")
result = palindrome((palabra.lower()).strip())
print(result)