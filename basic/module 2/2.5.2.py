# Filter

x = input().split()
xs = (int(i) for i in x)


def even(i):
    return i % 2 == 0

evens = filter(even, xs)

for e in evens:
    pass
    # print(e)

print(evens)