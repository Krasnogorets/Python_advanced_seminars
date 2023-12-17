"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""
import math


class Factorial:
    def __init__(self, start=None, stop=None):
        if stop is None:
            self.start = self.current = 1
            self.stop = start
            self.step = 1
        else:
            self.start = self.current = start
            self.stop = stop
            self.step = 1

    def __iter__(self):
        return self

    # def __next__(self):
    #     for i in range(self.start, self.stop, self.step):
    #         return math.factorial(i)
    #     raise StopIteration

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        result = self._calculate_factorial(self.current)
        self.current += self.step

        return result

    def _calculate_factorial(self, value):
        return 1 if value == 0 else value * self._calculate_factorial(value - 1)


f1 = Factorial(5, 10)
f2 = Factorial(7, 10)
f3 = Factorial(6)
print(f1)
for value in f1:
    print(value)
print(f2)
for value in f2:
    print(value)
print(f3)
for value in f3:
    print(value)
