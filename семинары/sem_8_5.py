"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.

"""
import pickle
import json
import os


def find_json(dir_name):
    for file_name in os.listdir(dir_name):
        if file_name.endswith('json'):
            file_name_net = file_name.split('.')[0]
            with open(file_name, 'r', encoding='utf8', newline='') as f:
                json_file = json.load(f)

                with open(f'{file_name_net}.pickle', 'wb') as w:
                    pickle.dump(json_file, w, protocol=pickle.DEFAULT_PROTOCOL)


find_json(os.getcwd())
