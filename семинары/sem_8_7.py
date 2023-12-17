import csv
import pickle

"""
Задание № 7
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""

def csv_to_pickle_string(csv_file_name):
    try:
        with open(csv_file_name, 'r', encoding='utf-8', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
            header = next(csv_reader)
            data = [row for row in csv_reader]

        pickle_string = pickle.dumps(data)
        print(pickle.loads(pickle_string))

    except FileNotFoundError:
        print(f'Файл не найден')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    csv_to_pickle_string('task_6.csv')