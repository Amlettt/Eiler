import math


def inp():
    chislo = int(input())
    return chislo


def schet(m):
    i = 3
    while i <= math.ceil(math.sqrt(m)):
        if m % i == 0:
            return False
        else:
            i += 2

    return True


def delitel():
    n = inp()
    z = 0
    if n != 0:
        i = 3
        while i <= int(n / 2):
            if schet(i) and n % i == 0:
                z = i
            i += 2
    print("Максимально простой делитель " + str(z))


delitel()
