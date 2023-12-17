"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from sem_14_2 import text_clean


def test_1():
    assert text_clean(' cksskjskdj skjdksi'), ' cksskjskdj skjdksi'


def test_2():
    assert text_clean('TTT cksskjskdj skjdksi'), 'ttt cksskjskdj skjdksi'


def test_3():
    assert text_clean('l, s ,e;l;3;l;s Ss'), 'l s ells ss'


def test_4():
    assert text_clean('которая Удаляет ИЗЗз текста text l, s ,e;l;3;l;s Ss'), '    text l s ells ss'


def test_5():
    assert text_clean('ФУНКкцию, RJNJоторая, '
                      'удаляет, из текста text '
                      'TTT 93939393 cksskjskdj '
                      'skjdksi T lse;l;3;l;s Ss'), ' rjnj    text ttt  cksskjskdj skjdksi t lsells ss'


if __name__ == '__main__':
    pytest.main(['-v'])
