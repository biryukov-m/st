import functools



def multer(m):
    temp = 1
    for cha in str(m):
        temp *= int(cha)
    return temp

# Refactored multer
def mu(m):
    return functools.reduce(lambda x, y: x*y, [int(i) for i in str(m)])

print(mu(44))


def persistence(n):
    cnt = 0
    while n > 9:
        print('Multing', n)
        n = multer(n)
        print('Result is', n)
        cnt += 1
    return cnt

print(persistence(25))
print(multer(39))