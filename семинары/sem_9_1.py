"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

from typing import Callable


def guess_num(a: int) -> Callable[[int], str]:
    def try_to_guess(b: int) -> str:
        for i in range(b):
            guess = int(input('введите число от 1 до 100:'))
            if guess == a:
                return 'вы угадали'
            else:
                print('вы не угадали, попробуйте еще')
        return 'кол-во попыток заончилось'

    return try_to_guess


secret_number = guess_num(25)
print(secret_number(10))
