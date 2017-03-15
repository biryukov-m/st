# Ввод
inma = []
a = []
while inma != ['end']:
    inma = input().split()
    if inma != ['end']:
        a += [inma]
# Вычисление

for i in range(len(a)):
    for j in range(len(a[i])):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ai = i + di
                aj = j + dj
                if 0 <= ai < len(a) and 0 <= aj < len(a[i]):
                    a[i][j] = a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]


# Вывод
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
