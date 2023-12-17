# a = input('введите текст: ')
# print(type(a), id(a), hash(a))
# help()
while True:
    a = input('введите текст: ')
    if a.isdigit():
        print(bin(int(a)),oct(int(a)), hex(int(a)))
    else:
        if a.isascii():
            print("ascii")
        else:
            print("not ascii")