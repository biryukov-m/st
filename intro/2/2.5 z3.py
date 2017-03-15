a = [int(i) for i in input().split()]
a.sort()
for i in range(0, len(a)-1):
        if a[i] == a[i+1] and a[i] != a[i-1]:
            print(a[i], end=' ')