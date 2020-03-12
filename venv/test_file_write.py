
list_small = [1, 2, 3]

with open('primer.txt', 'w') as file:
    file.write(str(list_small))

with open('primer.txt', 'r') as file:
    files = file.read()
    print(files)

