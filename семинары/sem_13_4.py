"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json


class User:
    users_dict = {}
    list_ids: list = []

    def __init__(self, name, user_id, access_level):
        self.name = name
        User.list_ids = self.recursive_items(User.users_dict)
        if user_id in User.list_ids:
            raise ValueError('id is exist')
        else:
            self.user_id = user_id
            User.list_ids.append(user_id)
        self.access_level = access_level
        try:
            User.users_dict[access_level][user_id] = name
        except KeyError:
            User.users_dict[access_level] = {}
            User.users_dict[access_level][user_id] = name
            print(User.users_dict)

    def recursive_items(self, dictionary):
        for key, value in dictionary.items():
            if type(value) is dict:
                yield from self.recursive_items(value)
            else:
                yield User.list_ids.append(key)

    def __str__(self):
        return f'LeveL: {self.access_level} id: {self.user_id} user name: {self.name}'


def create_users():
    while True:
        name = input("input name: ")
        user_id = input("input id: ")
        access_level = input("input access level: ")
        l = f'access level_{access_level}'
        try:
            User(name, user_id, l)
        except ValueError as e:
            print(e)
            continue
        # if user_id in b.get(l, {}):
        #     print("id is exist")
        #     continue
        # if l not in b:
        #     b[l] = {}
        # b[l][user_id] = name

        with open('sem_13_4.json', 'w', encoding='utf-8') as f:
            json.dump(User.users_dict, f, ensure_ascii=False, indent=2)


# print(User.list_ids)
create_users()
