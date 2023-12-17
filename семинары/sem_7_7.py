"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from pathlib import Path
import os


def sort_files(dir_1):
    file_names = check_dir(dir_1)
    for obj in file_names:
        ext = os.path.splitext(obj)[1].lower().replace('.', '')
        path = os.path.join(dir_1, obj)
        if not os.path.exists(os.path.join(dir_1, ext)):
            os.mkdir(os.path.join(dir_1, ext))
        new_path = os.path.join(dir_1, ext, obj)
        os.replace(path, new_path)


def check_dir(dir_1):
    return os.listdir(dir_1)


# sort_files('task_7_4_files')


def sort_files_1(dir2):
    folders = {'Video': ['.mp4', '.avi', '.mkv'], 'Pictures': ['.png', '.jpg', '.jpeg', '.gif', '.tiff'],
               'Texts': ['.txt', '.doc', '.docx', '.pdf']}
    if not os.path.exists(dir2):
        print('Указанная директория не существует')
    else:
        for dir2, _, files in os.walk(dir2):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                path = os.path.join(dir2, file)
                for k, v in folders.items():
                    if ext in v:
                        if not os.path.exists(os.path.join(dir2, k)):
                            os.mkdir(os.path.join(dir2, k))
                        new_path = os.path.join(dir2, k, file)
                        os.replace(path, new_path)


sort_files_1('task_7_4_files')
