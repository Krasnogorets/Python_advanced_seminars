"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from sem_14_2 import text_clean


class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(text_clean(' cksskjskdj skjdksi'), ' cksskjskdj skjdksi')

    def test_method1(self):
        self.assertEqual(text_clean('TTT cksskjskdj skjdksi'), 'ttt cksskjskdj skjdksi')

    def test_method2(self):
        self.assertEqual(text_clean('l, s ,e;l;3;l;s Ss'), 'l s ells ss')

    def test_method3(self):
        self.assertEqual(text_clean('которая Удаляет ИЗЗз текста text l, s ,e;l;3;l;s Ss'),'    text l s ells ss')

    def test_method4(self):
        self.assertEqual(text_clean('ФУНКкцию, RJNJоторая, '
                                    'удаляет, из текста text '
                                    'TTT 93939393 cksskjskdj '
                                    'skjdksi T lse;l;3;l;s Ss'),' rjnj    text ttt  cksskjskdj skjdksi t lsells ss')


if __name__ == '__main__':
    unittest.main()
