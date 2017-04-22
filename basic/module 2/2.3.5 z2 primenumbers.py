import itertools


def primes():
    i = 2
    while True:
        q = 0
        for j in range(2, i):
            if i % j == 0:
                q += 1
        if q == 0:
            yield i
        i += 1

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
