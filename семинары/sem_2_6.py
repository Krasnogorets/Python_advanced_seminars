'''

Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

_sum = 0
_count_add = 0
_count_out = 0

while True:
    if _sum > 5_000_000:
        _sum -= _sum * 0.1
        print('сняли налог на богатсво')
        print(_sum)
    command = input('ВВЕДИТЕ КОМАНДУ')
    if command == 'q':
        print('выходим из банкомата')
        print(_sum)
        break
    if command == 'a':
        sum_add = int(input('ВВЕДИТЕ СУММУ'))
        if sum_add % 50 == 0:
            _sum += sum_add
            _count_add +=1
            if _count_add % 3 == 0:
                _sum *= 1.03
        else:
            print("введена не кратная сумма 50")
    if command == 'o':
        sum_out = int(input('ВВЕДИТЕ СУММУ'))
        commision = sum_out * 0.015
        if commision <= 30:
            commision = 30
        elif commision > 600:
            commision = 600
        if (sum_out + commision) > _sum :
            print("средств не достаточно")
            print(_sum)
        else:
            if sum_out % 50 == 0:
                _count_out += 1
                if _count_out % 3 == 0:
                    _sum *= 1.03

    print(_sum)