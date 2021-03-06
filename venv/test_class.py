
class Person:

    people = 0

    def __init__(self, name):  # присвоит атрибуты к экземпляру класса
        self.name = name
        Person.people += 1

    def __del__(self):  # обязательно в конце удалит, если не удалилось до
        Person.people -= 1
        if Person.people == 0:
            print('{0} ушел. Никого не осталось.'.format(self.name))
        else:
            print('{0} ушел. Нас осталось всего {1}'.format(self.name, Person.people))

    def sayHi():
        print('Привет! Как жизнь нищеброд? Вас уже {0}'.format(Person.people))

    def sayName(self):
        print('Привет! Меня зовут {}'.format(self.name))

    # staticmethod говорит о том что метод не требует распознования в каком классе он находится как classmethod
    sayHi = staticmethod(sayHi)


p = Person('Пидор')
d = Person('Гомосек')
p.sayName()
d.sayName()
Person.sayHi()



