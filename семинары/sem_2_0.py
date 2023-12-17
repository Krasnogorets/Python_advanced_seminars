'''
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
'''
data = [1, 'text', True, 1.2 , b'123',None]
for item in data:
    print(type(item))
for i in range (1,len(data)):
    print(type(data[i]))

for item in data[1:]:
    print(type(data[i]))