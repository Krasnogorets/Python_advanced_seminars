"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:

    def __init__(self, age, first_name="unknown", last_name="unknown", patronymic_name="unknown"):
        self.__age = age
        self.first_name = first_name
        self._last_name = last_name
        self.patronymic_name = patronymic_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 100:
            raise ValueError('old')
        self.__age = value

    def full_name(self):
        return print(f'the full name is: {self._last_name} {self.first_name} {self.patronymic_name}')

    def birthday(self):
        self.__age += 1


p1 = Person(15, "Vasya", "Petrov")
p2 = Person(18, "Petya", "Ivanov", "Sergeevich")
p3 = Person(20, "Masha", "Gorina")
# print(p1.__age)
print(p1._Person__age)
p3.age = 80
p1.birthday()
p1.birthday()
p2.birthday()
print(p1.age)
print(p2.age)
print(p3.age)
p1.full_name()
p2.full_name()
p3.full_name()
