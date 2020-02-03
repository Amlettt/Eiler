import math


def solution():
    for a in range(3, 1000):
        for b in range(1, 1000):
            if a > b or a == b:
                continue
            c = math.sqrt(a * a + b * b)
            if c.is_integer():
                z = a + b + int(c)
                c1 = int(c)
                if z == 1000:
                    print("a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c1))
                    return a * b * int(c)


print(solution())
