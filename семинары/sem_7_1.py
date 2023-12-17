"""
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
from random import randint, uniform


def file_write(str_qts, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        for _ in range(str_qts + 1):
            print(f'{randint(-1000, 1001)}|{round(uniform(-1000, 1001),2)}', file=f)


file_write(5, 'task_7_1.txt')
