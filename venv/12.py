import math

i = 0
j = 164523960
# i = 0
# j = 1
m = 164523961
flag = True
while flag:
    i = 0
    j += m
    m += 1
    if j % 2 == 0:
        for k in range(3, int(j / 2)):
            if j % k == 0:
                i += 1
    if i + 4 > 400:
        print(j)
        flag = False 
