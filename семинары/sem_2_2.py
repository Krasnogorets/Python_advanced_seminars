'''
Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможн
'''
bin_base = 2
oct_base = 8
a: int = int(input('введите целое: '))
print(a, end=" ")
print(int(str(a), base=bin_base), end=" ")
print(int(a, base=oct_base), end=" ")