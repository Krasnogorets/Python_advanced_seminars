"""
Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
from sem_7_4 import file_creation
from pathlib import Path


def file_creation_with_dir(dir_1):
    try:
        Path(dir_1).mkdir()
        file_creation(file_type='7_6', path_1=dir_1, max_len=6)
    except FileExistsError:
        file_creation(file_type='7_6', path_1=dir_1, max_len=6)


file_creation_with_dir('task_7_4_files/')
