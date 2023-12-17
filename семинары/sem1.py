# task1
'''
Работа в консоли в режиме интерпретатора Python.
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c
'''
from math import sqrt

# a = 5
# b = -10
# c = -400
# d = b ** 2 - (4 * a * c)
# x1 = None
# x2 = None
#
# if d > 0:
#     x1 = (-1 * b + sqrt(d)) / (2 * a)
#     x2 = (-1 * b - sqrt(d)) / (2 * a)
#     print(x1, x2)
# elif d == 0:
#     x1 = (-1 * b) / (2 * a)
#     print(x1)
# elif d < 0:
#     print("корней нет", d)

# task2
'''
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n
'''
# n = int(input("введите n:"))
# e = int(input("введите e:"))
# i = 1
# _sum = 0
#
# while i <= n:
#     if i % 2 == 0 and i % e != 0:
#         _sum += i
#     i += 1
#
# print(_sum)

# task3
'''
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''
# year = int(input('введите год: '))
#
#
# def func_1(year):
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         year_type = 'високосный'
#     else:
#         year_type = 'не високосный'
#     return year_type
#
#
# def func_2(year):
#     return f' год {year} високосный' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else f' год {year} не ' \
#                                                                                                   f'високосный'
#
#
# print(f' год {year} ' + func_1(year))
# print(func_2(year))
# if year % 4 != 0:
#     year_type = 'не високосный'
# elif year % 100 == 0:
#     if year % 400 == 0:
#         year_type = 'високосный'
#     else:
#         year_type = 'не високосный'
# else:
#     year_type = 'високосный'
# print(year_type)

# task4
'''
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
'''

# while True:
#     n = int(input("введите число от 1 до 999: "))
#     if n < 1 or n > 999:
#         print("число не из диапазона")
#         continue
#     elif n < 10:
#         print(n ** 2)
#     elif 10 <= n < 100:
#         print((n % 10) * (n // 10))
#     elif n > 99:
#         res=0
#         while n != 0:
#             res = (res * 10) + (n % 10)
#             n //= 10
#         print(res)

# task5
'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
'''
# rows = 11
# _symbol = "*"
# _space = " "
# symbols = 1
# spaces = rows - 1
#
# for i in range (rows):
#     print(_space * spaces + _symbol * symbols + _space * spaces)
#     symbols += 2
#     spaces -= 1
#
# task6

'''
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
'''

for i in range (2, 10):
    for j in range (2,11):
        print(f'{i} X {j} = {i * j} ')
    print()