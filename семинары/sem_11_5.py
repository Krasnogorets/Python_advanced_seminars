"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Rectangle:

    def __init__(self, lenght, width=None):
        self.lenght = lenght
        if width is None:
            self.width = lenght
        else:
            self.width = width

    def perimetr(self):
        return 2 * (self.lenght + self.width)

    def square(self):
        return self.width * self.lenght

    def __add__(self, other):
        return Rectangle(self.perimetr() + other.perimetr())

    def __sub__(self, other):
        return Rectangle(abs(self.perimetr() - other.perimetr()))

    def __str__(self):
        return f'периметр = {self.perimetr()}'


c1 = Rectangle(10, 5)
c2 = Rectangle(5)
print(c1.perimetr())
print(c1.square())
print(c2.perimetr())
print(c2.square())
print(c1 + c2)
print(c1 - c2)
