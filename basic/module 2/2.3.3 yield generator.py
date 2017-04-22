from random import random


def random_gen(k):
    for i in range(k):
        yield random()
        print('Iteration - ', i+1)

g = random_gen(10)
# for i in g:
#     print(i)


def simple_gen():
    yield 1
    yield 2

for i in simple_gen():
    print(i)