"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""

import json
from os import path


def logger(func):
    try:
        with open(func.__name__ + '.json', 'r', encoding='utf8') as read_json:
            list_dict = json.load(read_json)
    except FileNotFoundError:
        print("файла пока нет")
        list_dict = []

    def wrapper(*args, **kwargs):
        list_dict.append({'args': args,
                          'kwargs': kwargs,
                          'result': func(*args, **kwargs)})
        with open(func.__name__ + '.json', 'w', encoding='utf8') as f:
            json.dump(list_dict, f, indent=2, ensure_ascii=False)

    return wrapper


@logger
def mean(*args, **kwargs):
    param_qts = len(args) + len(kwargs)
    param_sum = sum(args) + sum(kwargs.values())
    return param_sum / param_qts


@logger
def gmean(*args, **kwargs):
    param_qts = len(args) + len(kwargs)
    mult_params = 1
    for i in args:
        mult_params *= i
    for i in kwargs.values():
        mult_params *= i
    return mult_params ** (1 / param_qts)


if __name__ == '__main__':
    mean(5, 7, a=5, b=8)
    gmean(5, 7, a=5, b=8)
    mean(6, 3, a=10, b=5)
    gmean(8, 9, a=5, b=5)
