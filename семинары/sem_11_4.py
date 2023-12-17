"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя
"""


class Arhive:
    """Класс Arhive"""
    # num = None
    # text = None
    list_num = []
    list_txt = []

    def __init__(self, num, text):
        """метод __init__
        :param num - любое число
        :param text - любое текст
        """
        self.num = num
        self.text = text
        Arhive.list_num.append(num)
        Arhive.list_txt.append(text)

    def __str__(self):
        return f'Экземпляр класса {self.__class__}  num ={self.num}, text ={self.text}, ' \
               f'list_num = {self.list_num} list_txt = {self.list_txt} '

    def __repr__(self):
        return f'el ({self.num}, {self.text})'


a = Arhive(5, "5")
print(a)
b = Arhive(6, "6")
print(b)
c = Arhive(7, "7")
print(a)
print(b)
print(c)
print(repr(c))

# help(Arhive)
