"""
Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def buble_sort(lst_1) -> list:
    for i in range(len(lst_1)):
        for x in range(0, len(lst_1) - i-1):
            if lst_1[x] > lst_1[x + 1]:
                lst_1[x], lst_1[x + 1] = lst_1[x + 1], lst_1[x]
    return lst_1


print(buble_sort(lst))
