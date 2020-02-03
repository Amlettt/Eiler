import math

x = 0
y = 0
z = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        if str(x) == ''.join(reversed(str(x))):
            y = x
            if z < y:
                z = y

print(str(z))
