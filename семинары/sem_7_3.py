"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def combine_files():
    with (open('task_7_1.txt', 'r', encoding='utf-8') as f,
          open('sem_7_2.txt', 'r', encoding='utf-8') as c,
          open('sem_7_3.txt', 'w', encoding='utf-8') as d
          ):
        nums = f.readlines()
        names = c.readlines()
        long = max(len(list(nums)),len(list(names)))
        while len(nums) != len(names):
            if len(nums) > len(names):
                names.extend(names[:len(nums) - len(names)])
            else:
                nums.extend(nums[:len(names) - len(nums)])
        i = 0
        for_write = []
        while i < long:
            name = names[i]
            num = nums[i]
            a, b = map(float, num.split('|'))
            mult = a * b

            if mult >= 0:
                for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
            else:
                for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
            i += 1

        d.writelines(for_write)


combine_files()
