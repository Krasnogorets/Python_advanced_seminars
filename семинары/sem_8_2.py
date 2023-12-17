import json

"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
b = {}
while True:
    name = input("input name: ")
    user_id = input("input id: ")
    access_level = input("input access level: ")
    l = f'access level_{access_level}'
    if user_id in b.get(l, {}):
        print("id is exist")
        continue
    if l not in b:
        b[l] = {}
    b[l][user_id] = name

    with open('sem_8.2.json', 'w', encoding='utf-8') as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
