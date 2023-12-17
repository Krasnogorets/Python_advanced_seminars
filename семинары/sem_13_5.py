"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json


class User:
    """"""
    MIN_ACCESS_LEVEL = 1
    MAX_ACCESS_LEVEL = 7

    def __init__(self, name, user_id, access_level):
        """Constructor for User"""
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id},  level:{self.access_level}'

    def create_user_data_json(self):
        try:
            with open('sem_13_4.json', 'r', encoding='utf-8') as j_file:
                user_data = json.load(j_file)
        except FileNotFoundError:
            print('Файл не найден')
            user_data = {}

        while True:
            self.name = input('Введите имя или exit для выхода: ')
            if self.name.lower().strip() == 'exit':
                break

            self.user_id = input('Введите личный идентификатор (ID): ')
            self.access_level = input(
                f'Введите уровень доступа (от {User.MIN_ACCESS_LEVEL} до {User.MAX_ACCESS_LEVEL}): ')
            while self.user_id in user_data.values():
                print('Пользователь с таким ID уже существует. Попробуйте другой')
                self.user_id = input('Введите личный идентификатор (ID): ')

            if self.access_level not in user_data:
                user_data[self.access_level] = {}
            while self.user_id in user_data[self.access_level]:
                print("ID пользователя для этого уровня доступа уже существует. Попробуйте другой")
                self.user_id = input('Введите личный идентификатор (ID): ')

            user_data[self.access_level][self.user_id] = self.name

        with open('sem_13_4.json', 'w', encoding='utf-8') as j_file:
            json.dump(user_data, j_file, ensure_ascii=False, indent=2)

        print('Данные записаны')

    @staticmethod
    def load_user_data():
        try:
            with open('sem_13_4.json', 'r', encoding='utf-8') as j_file:
                user_data = json.load(j_file)
        except FileNotFoundError:
            print('Файл не найден')
            return set()

        users = set()

        for access_level, user_id_name in user_data.items():
            for user_id, name in user_id_name.items():
                user = User(name, user_id, int(access_level))
                users.add(user)
        return users


class UserException(Exception):
    pass


class UserLevelException(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня - level={self.value} меньше необходимого уровня)"


class UserAccessException(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка доступа"


class Project:
    def __init__(self):
        self.users = set()

    def load_data(self):
        self.users = User.load_user_data()

    def verification_login(self, name, user_id):
        login = User(name, user_id, 0)
        if login not in self.users:
            raise UserAccessException('Пользователь не найден')

        for user in self.users:
            if user == login:
                return user.access_level

    def add_user(self, name, user_id, access_level):
        new_user = User(name, user_id, access_level)
        for user in self.users:
            if user == new_user and user.access_level < access_level:
                raise UserLevelException('Вы не можете добавить пользователя с таким уровнем доступа')
        self.users.add(new_user)
        self._update_json_file()

    def _update_json_file(self):
        user_data = {}
        for user in self.users:
            if user.access_level not in user_data:
                user_data[user.access_level] = {}
            user_data[user.access_level][user.user_id] = user.name
        with open('sem_13_4.json', 'w', encoding='utf-8') as j_file:
            json.dump(user_data, j_file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    project = Project()
    project.load_data()

    # try:
    #     access_level = project.verification_login('User1', '123')
    #     print(f'Успешный вход. Уровень доступа: {access_level}')
    # except UserAccessException as e:
    #     print(f'В доступе отказано. {e}')

    # try:
    #     access_level = project.verification_login('Олег', '234')
    #     print(f'Успешный вход. Уровень доступа: {access_level}')
    # except UserAccessException as e:
    #     print(f'В доступе отказано. {e}')

    try:
        project.add_user('New_user', '256', 1)
        print('Пользователь успешно добавлен')
    except UserLevelException as e:
        print(f'Невозможно добавить пользователя. {e}')
