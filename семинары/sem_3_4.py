"""
Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды
"""
# lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
# for item in lst:
#     if item in lst:
#         lst.remove(item)
# print(lst)

# lst = [1, 2, 3, 4, 5]
lst = [1, 1, 2, 2, 3, 3]
dct = {}
for item in lst:
    dct[item] = dct.get(item, 0) + 1
new_lst = [el for el in lst if dct[el] >=2]
print(new_lst)

# lst = [1, 2, 3, 4, 5]
# print(*[el for el in lst if lst.count(el) != 2])