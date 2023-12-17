"""
Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""
text = "90 45"
num1 = int(text.split()[0])
num2 = int(text.split()[1])


def dct_crt(*args):
    if num1 > num2:
        start = num2
        finish = num1
    else:
        start = num1
        finish = num2
    dct = {}
    for el in range(start, finish + 1):
        dct[chr(el)] = el
    return dct


print(dct_crt(num1, num2))


def dct_crt_(a, b):
    return {chr(el):el for el in range(min(a, num2), max(num1, num2) + 1)}


print(dct_crt_(num1, num2))
