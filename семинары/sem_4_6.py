"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
lst = [1, 3, -5, 7, 5, 8, 4, -9, 2]

ind_1 = 2
ind_2 = 4


def sum_between(lst_1, a, b):
    if a > b:
        return print('no elements')
    elif a < 0 and b > len(lst_1):
        return sum(lst_1)
    elif a < 0:
        return sum(lst_1[:b])
    elif b > len(lst_1):
        return sum(lst_1[a + 1:])
    else:
        return sum(lst_1[a + 1:b])


print(sum_between(lst, ind_1, ind_2))
