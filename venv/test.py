s = 'dfgdf', 'dfsd'
m = (1, 2)
h = [1, 2]
g = {1: 2, 2: 3}
d = ''
a = 'Mama'
d = a

print('ma' in a)
print('{0} {1}'.format(g[2], g[1]))
say = {'lala', 'daddy', 'hello', 'mum'}
words = {'hello', 'daddy', 'hello', 'mum'}
print(say - words)

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))


# полидром тестим
# def cut(text):
#     text_mod = ""
#     simbol = ['^', '-', '_', ',', ':', ';', '(', ')', '\\', '|', '/', '?',
#               '!', ' ', '.', '[', ']', '{', '}', '"', "'", '%', '@', '#',
#               '$', '&', '=', '+', '~', '*']
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     for i in text.lower():
#         if i not in simbol or i not in numbers:
#             text_mod += i
#     return text_mod
#
# def polidrom(text):
#     m = cut(text)
#     return m[::-1]
#
# def reverse(text):
#     return cut(text) == polidrom(text)
#
# say = input("введи слово или фразу: ")
#
# print(reverse(say))


# два результата возврата функции
def return_result(x, y):
    return (x * y, x + y)


print(return_result(10, 20))
xy, x_y = return_result(10, 20)
z = return_result(10, 20)
print('z = {0}'.format(z))
print('x*y = {0},  x+y = {1}'.format(xy, x_y))

# два значения в одном результате
aa, *bb = [[1, 2, 3], 2, 3, 4]
print(aa[2])

cc, nn = 1, 2
cc, nn = nn, cc
print(nn)

# лямбда выражения (одноразовая функция) lambda arguments: expression
multiply = lambda x, y: x * y  # если присвоить переменной поведение как в обычной функции
print('Результат лямбда функции: %s' % multiply(21, 2))
colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
print(sorted(colors, key=lambda s: s.casefold()))

# сортировка списков
# sortList = ['a', 'dd', 'cc', 'bbb']
sortList = [1, 2, 5, 4, 3]
newlist = sorted(sortList)  # копирование списка через sorted
sortList.sort(reverse=True)
print(sortList)
print(newlist)


# Передача кортежей и словарей в функции
def powersum(power, *args): # после “*”, все дополнительные аргументы, переданные функции, сохранятся в args в виде кортежа
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print('Сумма аргументов powersum = {}'.format(powersum(2, 3, 4)))


# exec и eval
exec('print("Здравствуй, Мир!")')  # выполняет команду записанную как строка
print(eval('2*3'))  # считает выражение записанное как строка

# списки
list_ = [1, 2, 34, 1]
# list_[2], list_[3] = list_[3], list_[2]
print('list_ = {}'.format(list_))
list_[2::].sort()  # Сортировка части списка
print(list_)
print(list_.index(34))
