def schet():
    x = 1
    flag = True
    while flag:
        for i in range(1, 21):
            if not x % i == 0:
                break
            elif i == 20:
                return x

        x += 1


print(str(schet()))
