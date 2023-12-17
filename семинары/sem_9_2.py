"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""
import random

MIN_VAL = 1
MAX_VAL = 100
NAX_COUN = 10


def deco(func):
    def wrapper(a, b):
        if not MIN_VAL < a < MAX_VAL:
            print(f'ошибочное число {a}')
            a = random.randint(MIN_VAL, MAX_VAL)
            print(f'новое число {a}')
        if not MIN_VAL < b < NAX_COUN:
            print(f'ошибочное число {b}')
            b = random.randint(MIN_VAL, NAX_COUN)
            print(f'новое число {b}')
        return func(a, b)

    return wrapper


@deco
def try_to_guess(a, b):
    for i in range(b):
        guess = int(input('введите число от 1 до 100:'))
        if guess == a:
            return 'вы угадали'
        else:
            print(f'попытка{i} вы не угадали, попробуйте еще')
    return f'кол-во попыток закончилось {a}'


# try_to_guess = deco(try_to_guess)
print(try_to_guess(-1, 12))
