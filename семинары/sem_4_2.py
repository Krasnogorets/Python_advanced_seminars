"""
Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""
text = "Напишите функцию, которая принимает"


def _char_cplit(t):
    lst = []
    ch_lst = list(set(t))
    for ch in ch_lst:
        lst.append(ord(ch))
    return sorted(lst, reverse=True)


print(_char_cplit(text))


def _char_split(t):
    return sorted(set([ord(ch) for ch in t]), reverse=True)


print(_char_split(text))
