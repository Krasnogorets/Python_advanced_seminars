"""
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей
"""
data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Витя": ("Палатка", "Котелок", "Топор"),
        "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
        "Саша": ("Палатка", "Спирт")}

# Какие вещи взяли все три друга

lst = []
for k, v in data.items():
    lst.append(set(v))

print(lst)
for i in range(len(lst)-2):
    res = lst[1].intersection(lst[i + 1])
    new_res = res.intersection(lst[i + 2])

print(f' есть у всех: {new_res}')

# Какие вещи уникальны, есть только у одного друга

new_res_1 = set()

for key in data:
    res = set(data[key])
    for k in data:
        if key != k:
            res = res.difference(set(data[k]))
    if res:
        print(f'только {key} имеет вещи {res}')

# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует

for key in data:
    res = set(data[key])
    new_set = set()
    for k in data:
        if key != k:
            new_set = new_set.intersection(set(data[k])) if new_set else set(data[k])
    if new_set:
        d = new_set.difference(res)
        if d:
            print(f'только {key} не имеет {d}')