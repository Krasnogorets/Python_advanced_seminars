"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра

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
        return f'num ={self.num}, text ={self.text}, list_num = {self.list_num} list_txt = {self.list_txt}  '


a = Arhive(5, "5")
print(a)
b = Arhive(6, "6")
print(b)
c = Arhive(7, "7")
print(a)
print(b)
print(c)

# help(Arhive)
