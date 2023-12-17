"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


def count(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print(func(*args, **kwargs))
        return wrapper
    return decorator


@count(2)
def factorial(n):
    print(f'Вычисляю факториал {n}!')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


factorial(5)
