"""Каков порядковый номер первого члена последовательности Фибоначчи, содержащего 1000 цифр?"""


def fibonachi(x, x1):  # формула Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
    x1, x = x1 + x, x1
    return x, x1


count = 12  # начинаем с 12 итерации
number_fib1 = 89  # 11 число
number_fib2 = 144  # 12 число
flag = True

while flag:
    number_fib1, number_fib2 = fibonachi(number_fib1, number_fib2)
    count += 1
    if len(str(number_fib2)) >= 1000:
        print('Ответ: {}'.format(count))
        flag = False
        break
