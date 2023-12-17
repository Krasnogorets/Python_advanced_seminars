"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
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


c1 = Rectangle(10, 5)
c2 = Rectangle(5)
print(c1.perimetr())
print(c1.square())
print(c2.perimetr())
print(c2.square())
