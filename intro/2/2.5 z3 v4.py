a = [int(i) for i in input().split()]
a.sort()
i = 0
while i < len(a):
    if a.count(a[i]) > 1:
        print(a[i], end=' ')
    i += a.count(a[i])