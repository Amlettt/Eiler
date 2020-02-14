
class SchoolMember:  # базовый класс
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Новый сотрудник {0}'.format(self.name))

    def tell(self):
        print('Имя: "{0}", Возраст: "{1}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):  # Наследование базовых классов в виде кортежа
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # инициализыция части объекта относящегося к базовому классу
        self.salary = salary
        print('Создан учитель {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата {0}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан сутдент {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки {0}'.format(self.marks))


t = Teacher('Инвалид', '55', '15000')
s = Student('Лох', '19', '30')

t.tell()
