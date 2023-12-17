"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки
"""

str_1 = "пользователь вводит строку текста. вывести каждое слово с новой строки.".split()
lst_str_1 = sorted(str_1)
max_len = 0
for item in lst_str_1:
    if len(item) > max_len:
        max_len = len(item)

for index, el in enumerate(lst_str_1):
    print(f'{index} {el:>{max_len}}')
