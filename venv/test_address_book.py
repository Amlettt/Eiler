'''Создайте собственную программу «Адресная книга», работающую из командной стро-
ки и позволяющую просматривать, добавлять, изменять, удалять или искать контактные
данные ваших знакомых. Кроме того, эта информация также должна сохраняться на дис-
ке для последующего доступа.'''
import pickle  # библиотека для записи и открытия файла в бинарном состоянии
import argparse  # парсинг из команджной строки
import os


# class Address_book:
#     list_member = {}
#
#     def __init__(self, name, script):
#         self.name_book = name
#         self.script = script
#
#
# def new(name_book, name, script):
#     assert not isinstance(name_book, Address_book)
#     name_book = Address_book(name, script)
#     return name_book


def add(list_):  # assert выдаст ошибку если условие неправильное, проверяем есть ли пользователь в словаре
    assert list_[0] not in data.keys()
    data[list_[0]] = (list_[1], list_[2])
    print('Адрес "{}" добавлен.'.format(list_[0]))


def update(list_):
    assert list_[0] in data.keys()
    data[list_[0]] = (list_[1], list_[2])
    print('Адрес "{}" изменен.'.format(list_[0]))


def delete(name):
    for i, key in enumerate(data.keys()):
        if key == name:
            del data[key]
            print('Адрес "{}" удален.'.format(name))
            break
        elif i == len(data.keys()) - 1:
            print('Контакт с именем {} не существует.'.format(name))


def find(name):
    for i, key in enumerate(data.keys()):
        if key == name:
            print('{0} - {1}'.format(key, data[key]))
        elif i == len(data.keys())-1:
            print('Контакт с именем {} не найден.'.format(name))


def show():
    if data:
        for key, value in data.items():
            print('{0} - {1}'.format(key, value))
    else:
        print('В адресной книгне нет записей')


def createParser():
    # указываем что это за парсер, кто автор, всякую инфу
    parser = argparse.ArgumentParser(description='Acсess to address book')
    # nargs ='*' говорит что создаст список параметров, их можно от 0 и больше указать.
    # если nargs = 1 или 2,3 тоже создаст список из этого указанного кол-ва
    parser.add_argument('-new', nargs='*', type=str, help='new address book. 3 parametres: name_book, name, script')
    parser.add_argument('-add', nargs='*', type=str, help='add new address. 3 parametres: name, address, phone')
    parser.add_argument('-update', nargs='*', type=str, help='update old address . 3 parametres: name, address, phone')
    # nargs ='?' то он не создает список, а принимает кол-во параметров 0 или 1, как тупо значение
    parser.add_argument('-delete', nargs='?', type=str, help='delete exist address. parametres: name')
    parser.add_argument('-find', nargs='?', type=str, help='find address, if it exist in book. 3 parametres: name')
    parser.add_argument('-show', nargs='?', const=1, help='show all address in book. Without parametres')
    return parser


if __name__ == "__main__":
    parser = createParser()  # экземпляр парсера
    args = parser.parse_args()  # в скобках можно парсить из программы ['-команда', 'значение параметра']
    try:
        f = open('data.pickle', 'rb')  # открываем файл, если пустой получим ошибку. Неработает.
        data = pickle.load(f)  # все данные записываем в data
        # print(data)
        f.close()
    except EOFError:
        print('Нет ни одной адресной книги.')

    if args.new:  # если в командной строке записана команда -new
        list_param = list(i for i in args.new)
        book = new(list_param)

    if args.add:
        add(args.add)

    if args.update:
        update(args.update)

    if args.delete:
        delete(args.delete)

    if args.find:
        find(args.find)

    if args.show:
        show()

    with open('data.pickle', 'wb') as f:  # Сохраняем изменения внесенные во время работы с программой
        pickle.dump(data, f)
