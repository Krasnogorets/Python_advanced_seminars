"""На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры."""

import pytest
from user import *


@pytest.fixture
def func():
    obj = CheckUserLogin()
    obj.load_users()
    return obj


def test_access(func):
    assert func.get_login_level('Новиков') == 'Пользователь найден'


def test_except(func):
    with pytest.raises(NameErr):
        func.get_login_level('Федоров')


if __name__ == '__main__':
    pytest.main(['-v'])

