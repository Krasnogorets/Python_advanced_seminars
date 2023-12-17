'''
Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
'''
from math import sqrt
import cmath

a = 10
b = -50
c = 100
d = b ** 2 - (4 * a * c)


if d > 0:
    x1 = (-1 * b + sqrt(d)) / (2 * a)
    x2 = (-1 * b - sqrt(d)) / (2 * a)
    print(x1, x2)
elif d == 0:
    x1 = (-1 * b) / (2 * a)
    print(x1)
elif d < 0:
    x1 = (-1 * b + cmath.sqrt(complex(d))) / (2 * a)
    x2 = (-1 * b - cmath.sqrt(complex(d))) / (2 * a)
    print(x1, x2)

