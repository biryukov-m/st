list = input().split()
list.sort()
i = 0
while i < len(list):
    if list.count(list[i]) > 1:
        print(list[i], end=' ')
    i += list.count(list[i])