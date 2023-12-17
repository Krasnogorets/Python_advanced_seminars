"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import json
import csv


def save_csv():
    # new_dict = {}
    with (open('sem_8.2.json', 'r', encoding='utf8') as f,
          open('sem_8_3.csv', 'w', newline='', encoding='utf-8') as w):
        new_dict = json.load(f)
        # print(new_dict)
        csv_writer = csv.writer(w)
        csv_writer.writerow(['acces_level', 'id', 'name'])
        for acces_level, user_data in new_dict.items():
            for user_id, name in user_data.items():
                csv_writer.writerow([acces_level, user_id, name])


save_csv()
