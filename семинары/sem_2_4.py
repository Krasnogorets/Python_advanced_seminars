'''
Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.

'''

import decimal
from logging import exception

PI: decimal = 3.14159265358979323846_2643383279_5028841971_6939937510_5820974944_5923078164_0628620899_8628034825
while True:
    try:
        diametr: decimal = decimal.Decimal(input("введите диаметр: "))
    except ValueError:
        print('ошибка')
    if 1 < diametr < 1_000:
        decimal.getcontext().prec = 42
        square: decimal = decimal.Decimal(PI) * (diametr / decimal.Decimal(2)) ** 2
        # l = PI * diametr
        print(f' площадь {square} ')
    finally:
        print()
