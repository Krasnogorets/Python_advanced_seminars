"""
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков
"""
list_1 = [1, 2, 3, 4, 4, 1, 23, 3, 4, 7, 8, 8, 4, 4, 3, 5]
print(list_1)
print(set(list_1))
list_3 = []

for i in range(len(list_1)):
    flag = False
    for j in range(len(list_3)):
        if list_1[i] == list_3[j]:
            flag = True
    if not flag:
        list_3.append(list_1[i])

print(list_3)

list_4 = []
for item in list_1:
    if item not in list_4:
        list_4.append(item)
print(list_4)