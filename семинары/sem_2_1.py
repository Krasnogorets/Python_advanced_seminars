'''
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''
import sys

data = [5, 5, "string", 0.15, True, None, (1, 2), (1 ,2 ) ]
# for i in range(len(data)):
#     print(i + 1, data[i], id(data[i]), sys.getsizeof(data[i]), end=" ")
#     if hash(data[i]):
#         print(hash(data[i]), end=" ")
#     if isinstance(data[i], int):
#         print("целое", end=" ")
#     if isinstance(data[i], str):
#         print("строка", end=" ")
#     print()

for i, value in enumerate(data, 1):
    print(f'{i} {value} {id(value)} {sys.getsizeof(value)} {hash(value)}')
    if type(value) == int and value > 0:
        print("целое")
    elif type(value) == str:
        print("строка")