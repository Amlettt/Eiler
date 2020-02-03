import math
i=2031120
j=2031121
# i = 0
# j = 1
m = 2
flag = True
while flag:
    i = 0
    j += m
    m += 1
    if j % 2 == 0:
        for k in range(2, int(j / 2) + 1):
            if j % k == 0:
                i += 1
    if i + 2 > 200:
        print(j)
        flag = False
