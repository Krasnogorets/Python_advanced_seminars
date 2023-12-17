"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""


class Person:

    def __init__(self, age, first_name="unknown", last_name="unknown", patronymic_name="unknown"):
        self.__age = age
        self.first_name = first_name
        self._last_name = last_name
        self.patronymic_name = patronymic_name

    def get_current_age(self):
        return print(f'the age of {self.first_name} is: {self.__age}')

    def full_name(self):
        return print(f'the full name is: {self._last_name} {self.first_name} {self.patronymic_name}')

    def birthday(self):
        self.__age += 1


class Worker(Person):
    def __init__(self, id_id, *args, **kwargs):
        if len(str(id_id)) == 6:
            self.id_id = id_id
        self.level = sum(int(i) for i in str(id_id)) % 7
        super().__init__(*args, **kwargs)


w1 = Worker(444444, 40, 'IVAN', 'SMOLYAR')
print(w1.level)
