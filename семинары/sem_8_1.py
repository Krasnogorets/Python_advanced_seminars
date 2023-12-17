import json
"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
new_dict = {}


with open('sem_7_3.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
for line in lines:
    new_dict[line.split(' - ')[0].lower().capitalize()] = line.split(' - ')[1]

# print(new_dict)
with open('sem_8_1.json', 'w') as f:
    json.dump(new_dict, f, indent=2, ensure_ascii=False)
