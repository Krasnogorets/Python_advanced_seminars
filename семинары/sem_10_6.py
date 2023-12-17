"""
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def get_kind(self):
        return self.kind

    def get_name(self):
        return self.name
