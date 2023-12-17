"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


#
# def input_num() -> int | float:
#     while True:
#         try:
#             num = float(input('Введите целое или вещественное число: '))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#
#     return num
#
#
# number = input_num()
# print(f'= {number} ')

def input_num() -> int | float:
    while True:
        num = input('Введите целое или вещественное число: ')
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError as e:
                print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                      f'Попробуйте снова')


number = input_num()
print(f'= {number} ')