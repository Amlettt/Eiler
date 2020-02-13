"""
Подсчитайте сумму всех дружественных чисел меньше 10000.
"""
import math

s = []  # список найденных дружественых чисел
a = []  # временные хранилища делителей
b = []

for i in range(1, 10000):
    a.clear()
    b.clear()
    if i not in s:
        for j in range(math.ceil(i / 2)):  # ищем делители числа i
            if i % (j + 1) == 0:
                a.append(j+1)
        h = sum(a)  # считаем сумму делителей чтобы ее проверить на ее делители
        if h < 10000:  # считаем числа только меньше 10000
            for k in range(math.ceil(h / 2)):  # ищем делители числа i
                if h % (k + 1) == 0:
                    b.append(k+1)
            d = sum(b)
            if i == d and i != h:  # проверка на дружественность чисел
                s.append(i)
                s.append(h)

print(sum(s))
