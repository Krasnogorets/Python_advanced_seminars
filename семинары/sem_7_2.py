"""
Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
sonants = ['a', 'e', 'i', 'o', 'u']


def names_generator(names_qts):
    for _ in range(names_qts):
        c = ""
        for i in range(randint(4, 8)):
            if i == 0:
                c += consonants[randint(0, 20)].upper()
            else:
                o = randint(0, 1)
                if o == 1:
                    c += consonants[randint(0, 20)]
                else:
                    c += sonants[randint(0, 4)]
        with open('sem_7_2.txt', 'a', encoding='utf-8') as f:
            f.write(f'{c}\n')


names_generator(5)
