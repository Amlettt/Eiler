"""
Сумма цифр факториала 100!
"""

summa = 0
fac = 1
# считаем факториал
for i in range(2, 101):
    fac *= i
# считаем сумму цифр полученного факториала
for j in str(fac):
    summa += int(j)
print(summa)
