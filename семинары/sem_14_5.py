"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.

"""
import unittest


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


class TestCaseName(unittest.TestCase):
    def setUp(self) -> None:
        self.c2 = Rectangle(5)
        self.c1 = Rectangle(10, 5)
        self.c3 = Rectangle(14, 6)

    def test_method_1(self):
        self.assertRaisesRegex(ValueError, 'значение отрицательное', Rectangle, -10, 5)

    def test_method_2(self):
        self.assertRaisesRegex(ValueError, 'значение отрицательное', Rectangle, 10, -5)

    def test_method_3(self):
        self.assertEqual(Rectangle(10, 5), Rectangle(5, 10))

    def test_method_4(self):
        self.assertEqual(self.c2.width, self.c2.lenght)

    def test_method_5(self):
        self.assertEqual(self.c1.perimetr(), 30)

    def test_method_6(self):
        self.assertEqual(self.c1.square(), 50)

    def test_method_7(self):
        self.assertEqual(self.c1 + self.c2, Rectangle(50))

    def test_method_8(self):
        self.assertTrue(self.c1 > self.c2)

    def test_method_9(self):
        self.assertFalse(self.c1 == self.c3)


if __name__ == '__main__':
    # c1 = Rectangle(-10, 5)
    # print(c1)
    unittest.main(verbosity=2)
