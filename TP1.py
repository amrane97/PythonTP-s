
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

print('veuillez insere un nombre entier positif : ')
f = sycaruse(int(input()))