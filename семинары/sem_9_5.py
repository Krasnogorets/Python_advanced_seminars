"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""

import random
import json
from functools import wraps

MIN_VAL = 1
MAX_VAL = 100
NAX_COUN = 10


def logger(func):
    print('запускаю декоратор записи в файл')
    try:
        with open(func.__name__ + '.json', 'r', encoding='utf8') as read_json:
            list_dict = json.load(read_json)
    except FileNotFoundError:
        list_dict = []

    def wrapper(*args, **kwargs):
        list_dict.append({'загаданное число': args[0],
                          'кол-во попыток': args[1],
                          'result': func(*args, **kwargs)})
        with open(func.__name__ + '.json', 'w', encoding='utf8') as f:
            json.dump(list_dict, f, indent=2, ensure_ascii=False)

    return wrapper


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not MIN_VAL < args[0] < MAX_VAL:
            my_list = list(args)
            print(f'ошибочное число {my_list[0]}')
            my_list[0] = random.randint(MIN_VAL, MAX_VAL)
            args = tuple(my_list)
            print(f'новое число {args[0]}')
        if not MIN_VAL < args[1] < NAX_COUN:
            my_list = list(args)
            print(f'ошибочное число {my_list[1]}')
            my_list[1] = random.randint(MIN_VAL, NAX_COUN)
            args = tuple(my_list)
            print(f'новое число {args[1]}')
        return func(*args, **kwargs)

    return wrapper


def count(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return decorator


@count(2)
@deco
@logger
def try_to_guess(a, b):
    for i in range(b):
        guess = int(input('введите число от 1 до 100:'))
        if guess == a:
            print('вы угадали')
            return True
        else:
            if a < guess:
                print(f'попытка{i} вы не угадали, загаданное число меньше {guess} попробуйте еще')
            else:
                print(f'попытка{i} вы не угадали, загаданное число больше {guess} попробуйте еще')
    print(f'кол-во попыток закончилось, верное число {a}')
    return False


# try_to_guess = deco(try_to_guess)
try_to_guess(200, 12)
