import math


def isperfect(n):
    try:
        return pow(n, 0.5) % 1 == 0
    except:
        return False

for i in range(233456452):
    if isperfect(i):
        print(i)