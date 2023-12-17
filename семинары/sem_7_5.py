"""
 Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

"""
from sem_7_4 import file_creation
from random import randint


def file_creation_new(ext, file_qts=3):
    for el in ext:
        file_creation(el, min_len=6, max_len=10, files_qts=randint(file_qts, 5))


file_creation_new(['txt', 'www', 'bytes', 'go'])
