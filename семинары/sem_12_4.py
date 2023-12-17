"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:

    def __init__(self, lenght, width=None):
        self.lenght = lenght
        if width is None:
            self.width = lenght
        else:
            self.width = width

    @property
    def lenght(self):
        return self._lenght

    @property
    def width(self):
        return self._width

    @lenght.setter
    def lenght(self, value):
        if value > 0:
            self._lenght = value
        else:
            raise ValueError(f'значение отрицательное')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'значение отрицательное')

    def perimetr(self):
        return 2 * (self._lenght + self._width)

    def square(self):
        return self._width * self._lenght

    def __add__(self, other):
        return Rectangle(self.perimetr() + other.perimetr())

    def __sub__(self, other):
        return Rectangle(abs(self.perimetr() - other.perimetr()))

    def __str__(self):
        return f'периметр = {self.perimetr()}, площадь = {self.square()}'

    def __eq__(self, other):
        return self.square() == other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()


c1 = Rectangle(10, 5)
c1.width = 10
c3 = Rectangle(14,6)
c2 = Rectangle(5)
# print(c1.perimetr())
# print(c1.square())
# print(c2.perimetr())
# print(c2.square())
# print(c1 + c2)
# print(c1 - c2)
print(c1 > c2)
print(c1 < c2)
print(c1 == c3)
print(c1 != c2)
print(c1 <= c2)
