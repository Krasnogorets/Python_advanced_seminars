"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""


def text_clean(text):
    res = ''
    for char in text.lower():
        if ord(char) == 32 :
            res += char
        if 97 <= ord(char) <= 122:
            res += char
    return res


print(text_clean('функцию, которая удаляет из текста text TTT 93939393 cksskjskdj skjdksi T lse;l;3;l;s Ss'))
