"""Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только

вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.

Сколько существует таких маршрутов в сетке 20×20?

"""
# k = []
# m = []
# for t in range(21):
#     for o in range(21):
#         m.append(o)
#     k.append(m.copy())
#     m.clear()
#
#
# def _iter(i):
#     count = 0
#     if k[0][-i] != 0:
#         count = right()
#     else:
#         down()
#     return count
#
#
# def right():
#     count = 0
#     for j in range(2, 22):
#         if k[i][j] != '':
#             count += 1
#     return count
#
#
# def down():
#     pass
#
#
# p = 0  # p количество итераций по столбцам от предпоследнего к первому
# for i in range(20):
#     p = _iter(i)

n = 3
b = 0
for i in range(1, n):
    if i == 1:
        d = n + 1
    # elif i == 2:
    #     d = d*3
    else:
        d = d*2
    b += d
print(b + b)
