from math import *

z = 17

for i in range(9, 2000001, 2):
    j = 3
    while j <= ceil(sqrt(i)):
        if i % j == 0:
            break
        if j >= int(sqrt(i)):
            z += i
        j += 2
print(z)
