from operator import truediv
from pickle import TRUE

def palindrome(nombre):
    band= False
    alreves= nombre[::-1]
    if nombre == alreves:
        band= True

    return band 

result = palindrome("tuberculos")
print(result)