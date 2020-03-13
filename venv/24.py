"""
Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

"""

import math


def shift(lst, indx, indx1, indx2):  # сдвиг чисел, меняем местами (список, размер списка, что меняем, на что меняем)
    lst[indx1], lst[indx2] = lst[indx2], lst[indx1]  # замена чисел местами
    if indx1 < indx - 1:  # сортировка после замены если заменяемый индекс был дальше предпоследнего числа
        lst[(indx1+1)::] = sorted(lst[indx1+1::])
    return lst


list_number = [i for i in range(10)]  # создаем список
count_iter = 1  # счетчик итераций

flag = True
len_list = len(list_number)-1  # переменная для работы с индексом списка

while flag:
    flags = True
    i = 0
    while flags:
        i += 1
        if count_iter == 1000000:
            print('Милионная перестановка = {}'.format(list_number))
            flag = False
            break
        # сравниваем последнее и прдпоследнее если последнее больше то меняем местами
        if list_number[len_list-i] < list_number[len_list]:
            count_iter += 1
            list_number = shift(list_number, len_list, len_list-i, len_list)
            print('{0} = {1}'.format(count_iter, list_number))
            break
        # если итый индекс меньше чем одно из оставшихся чисел списка, то находим число которое следующее после него
        # и менеям их местами
        if list_number[len_list-i] < max(list_number[(len_list-i+1)::]) and i <= len_list:
            for n in sorted(list_number[(len_list - i + 1)::]):  # отсортировали часть списка и его итерируем
                if n > list_number[len_list-i]:  # если число из отсор. списка больше чем итое будем их менять
                    min_ = list_number.index(n)
                    break
            list_number = shift(list_number, len_list, len_list - i, min_)
            count_iter += 1
            print('{0} = {1}'.format(count_iter, list_number))
            break
