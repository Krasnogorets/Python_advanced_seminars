"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time


class MyString(str):

    def __new__(cls, author, text, *args, **kwargs):
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time_of_creation = time.strftime('%H:%M:%S')
        return instance


a = MyString('filipp', 'jkdjkkfdsklsdkjkdjksdk')
print(a, a.author, a.time_of_creation)
