"""
Создайте класс с базовым исключением и дочерние класс -исключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class UserException(Exception):
    pass


class AccessError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'код {self.value} не верный'


class LevelError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'уровень должен быть 1-5, а здесь {self.value}'




class User:
    CODE = '000'
    MIN_LEVEL = 1
    MAX_LEVEL = 5

    def __init__(self, level, code: str):
        if self.MIN_LEVEL <= level <= self.MAX_LEVEL:
            self.level = level
        else:
            raise LevelError(level)
        if code != self.CODE:
            raise AccessError(code)
        else:
            print(f'{self.__class__} code accepted')
            pass


user1 = User(2,'000')
# user2 = User(2,'009')
# print(User.__dict__)