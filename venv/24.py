"""
Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

"""

import math

list_number = [i for i in range(3)]
# list_number.reverse()
count_iter = 1

# for i in range(2, 4):
#     for j in range(1, i+1):
#         if j > j+1:
#             count_iter += 1


def shift(lst, indx):
    lst.append(lst.pop(indx))


def change(lst, indx):
    lst.insert(indx, lst.pop(indx + 1))


print("{0} = {1}".format(count_iter, list_number))

# for i in range(len(list_number)-1, 0, -1):
#     index = i - 1
#     list_number_copy = list_number.copy()
#
#     for j in range(math.factorial(len(list_number)-i)-1):
#
#         if list_number_copy[i] > list_number_copy[i-1]:
#             shift(list_number_copy, index)
#             count_iter += 1
#             print("{0} = {1}".format(count_iter, list_number_copy))
#             index -= 1
#         else:
#             change(list_number_copy, index)
#             count_iter += 1
#             print("{0} = {1}".format(count_iter, list_number_copy))


pointer = len(list_number) - 2
index = pointer
flag = True

for i in range(1, len(list_number)-1):
    list_number_copy = list_number.copy()
    j = 0

    while pointer >= 0:
        if flag:
            change(list_number_copy, index)
            count_iter += 1
            flag = False
            print("{0} = {1}".format(count_iter, list_number_copy))

            if index == len(list_number) - 2:
                pointer -= 1
                index = pointer
                flag = True
                continue
            else:
                index += 1
                continue


        # if list_number_copy[index] > list_number_copy[index + 1]:
        #     shift(list_number_copy, index)
        #     count_iter += 1
        #     print("{0} = {1}".format(count_iter, list_number_copy))
        #     index -= 1
        # else:
        #     change(list_number_copy, index)
        #     count_iter += 1
        #     print("{0} = {1}".format(count_iter, list_number_copy))

        j += 1

        if count_iter == 1000000:
            print(list_number_copy)
            break


            







