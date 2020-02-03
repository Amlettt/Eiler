import math

i = 6
z = 15
while i < 10001:
    z += 2
    for j in range(2, int(math.sqrt(z)) + 1):
        if z % j == 0:

            break
        elif j == int(math.sqrt(z)):

            i += 1

print(z)
