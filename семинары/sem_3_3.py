"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа
"""
# tup = (1, 2, 3, 'eee', 'ttt', 3.4, -0.12, [1, 2, 3], ['eee', 'ttt'])
tup = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')
dict_1 = {}
for item in tup:
    obj_type = type(item)
    list_1 = []
    for el in tup:
        if type(el) == obj_type:
            list_1.append(el)
    dict_1[obj_type] = list_1
print(dict_1)

data = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')

result_dict = dict()

for el in data:
    el_type = str(type(el))
    if el_type not in result_dict.keys():
        result_dict[el_type] = [el]
    else:
        result_dict[el_type].append(el)
print(result_dict)