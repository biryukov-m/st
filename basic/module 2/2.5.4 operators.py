import operator as op

# Операторы для операций с числами
print(op.add(4,5))
print(op.mul(4,5))

# Вытягивание из списка числа, т.е. по сути - реализация квадратных скобок x[n]
x = [1, 2, 3]
f = op.itemgetter(1)
print(f(x))

# Вытягивание из словаря по ключу, т.е. по сути - реализация квадратных скобок x['key']
x = {'123': 3324}
f = op.itemgetter('123')
print(f(x))

# attrgetter
f = op.attrgetter('sort')  # f(x) == x.sort
print(f([]))