"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import pickle
import csv
from typing import List, Any


def pickle_to_csv_tab(file_name):
    try:
        file_name_csv = file_name.split('.')[0] + ".csv"
        with (open(file_name, 'rb') as f,
             open(file_name_csv, 'w' , encoding='utf-8', newline='') as csv_f):

            data = pickle.load(f)
            # print(new_dict)
            header = data.keys()
            print(header)
            csv.writer = csv.DictWriter(csv_f, fieldnames=header)
            csv.writer.writeheader()
            csv.writer.writerows(data)
            # print(recursive_dict_print(new_dict))
    except FileNotFoundError:
        print('file not found')
    except Exception as e:
        print(e)






pickle_to_csv_tab('sem_8_4.pickle')
