"""
Есть список имен в файле names.txt
Если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого
 по буквам 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке.
Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
"""

Summa = 0

with open('../names.txt', 'r') as name:
    Names = name.read()
    Names = Names[1:-1]
    list_names = Names.split('","')
    list_names.sort()  # сортировка списка по алфавиту
    for iter_number, i in enumerate(list_names, 1):
        # print(i)
        char_number = 0
        # считаем сумму номеров букв имен. вычитаем 64 так как в юникоде А=65
        for j in i:
            char_number += ord(j) - 64
        # премножаем сумму номеров имени с итерацией
        Summa += iter_number*char_number
print(Summa)
