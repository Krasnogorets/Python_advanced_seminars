"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def lenth(self):
        return 2 * self.radius * math.pi

    def square(self):
        return math.pi * self.radius ** 2


c1 = Circle(10)
print(c1.lenth())
print(c1.square())
