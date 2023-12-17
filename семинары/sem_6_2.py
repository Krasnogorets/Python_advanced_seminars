from guess_num.guess_num import func
from sys import argv

lst = ([int(el) for el in argv[1:]])
a, b, c = map(int, lst)
func(a, b, c)
