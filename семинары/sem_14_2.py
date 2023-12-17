"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


def text_clean(text):
    """
    функция, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре
    :param text: str
    :return: str
    >>> text_clean(' cksskjskdj skjdksi')
    ' cksskjskdj skjdksi'
    >>> text_clean('TTT cksskjskdj skjdksi')
    'ttt cksskjskdj skjdksi'
    >>> text_clean('l, s ,e;l;3;l;s Ss')
    'l s ells ss'
    >>> text_clean('которая Удаляет ИЗЗз текста text l, s ,e;l;3;l;s Ss')
    '    text l s ells ss'
    >>> text_clean('ФУНКкцию, RJNJоторая, удаляет, из текста text TTT 93939393 cksskjskdj skjdksi T lse;l;3;l;s Ss')
    ' rjnj    text ttt  cksskjskdj skjdksi t lsells ss'
    """

    res = ''
    for char in text.lower():
        if ord(char) == 32:
            res += char
        if 97 <= ord(char) <= 122:
            res += char
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # text_clean('ФУНКкцию, RJNJоторая, удаляет, из текста text TTT 93939393 cksskjskdj skjdksi T lse;l;3;l;s Ss')
# text_clean('функцию текста text TTT 93939393 skjdksi T lse;l;3;l;s Ss')
