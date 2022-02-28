
from os import remove


def sycaruse(n):

    while (n != 1):
        if (n % 2 == 0 and n > 0):
            n = n//2
            print(n)
        elif (n % 2 == 1 and n > 0):

            n = n*3 + 1
            print(n)

    return n

def mul_egyptienne(a,b):
    
    s = 0
    while a != 0:
        if a % 2 == 1:
            s += b
        a = a // 2
        b +=  b

    print(s)

print ("Veuillez inserez deux chiffres : ")
a = int(input("chiffre1 : "))
b = int(input("chiffre 2 : "))
mul_egyptienne(a, b)

