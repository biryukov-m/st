import random
from time import sleep


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random.randint(0, self.k)

x = RandomIterator(10)