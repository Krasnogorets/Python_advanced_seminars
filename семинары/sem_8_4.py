"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import json, csv


def load_and_save(csv_file, json_file):
    with (open(csv_file, 'r', encoding='utf8', newline='') as f,
          open(json_file, 'w') as w):
        csv_data = csv.reader(f)
        l = {}
        for i, line in enumerate(csv_data):

            if i == 0:
                continue
            line[1] = f'{line[1]}:010'
            line[2] = str(line[2]).capitalize()
            line.append(hash(line[1] + line[2]))
            # print(line)
            l[line[0]] = {'user_data': {"user_id": line[1], "user_name": line[2],"hash": line[3]}}
        json.dump(l, w, indent=2, ensure_ascii=False)


load_and_save('sem_8_3.csv', 'sem_8_4.json')
