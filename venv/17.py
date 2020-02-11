"""
Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно

без пробелов, только буквы?

"""
numbers = {'числа': ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                     'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
                     'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                     'nineteen'],
           'десятки': ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                       'seventy', 'eighty', 'ninety'],
           'сотня': 'hundred',
           'сотни': 'hundredand'}


def counter_(i):
    string_number = list(map(int, str(i)))
    if i < 20:
        return len(numbers['числа'][i - 1])
    elif 20 <= i < 100:
        if 0 in string_number:
            return len(numbers['десятки'][string_number[0] - 2])
        else:
            return sum([len(numbers['десятки'][string_number[0] - 2]),
                       len(numbers['числа'][string_number[1] - 1])])
    else:
        if i % 100 == 0:
            return sum([len(numbers['числа'][string_number[0] - 1]),
                       len(numbers['сотня'])])
        elif string_number[1] < 2:
            return sum([len(numbers['числа'][string_number[0] - 1]),
                       len(numbers['сотни']),
                       len(numbers['числа'][int(str(string_number[1]) + str(string_number[2])) - 1])])
        elif string_number[2] == 0:
            return sum([len(numbers['числа'][string_number[0] - 1]),
                       len(numbers['сотни']),
                       len(numbers['десятки'][string_number[1] - 2])])
        else:
            return sum([len(numbers['числа'][string_number[0] - 1]),
                       len(numbers['сотни']),
                       len(numbers['десятки'][string_number[1] - 2]),
                       len(numbers['числа'][string_number[2] - 1])])


counter = 11  # 11 - это включено число 1000 (one thousand)
for i in range(1, 1000):
    counter += counter_(i)

print(counter)
