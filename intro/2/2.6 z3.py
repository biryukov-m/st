lst = list(range(1, 1555))
lst.reverse()
x = 234
# x = int(input())


# Вариант 1
if x in lst:
    for i in range(0, len(lst)):
        if int(lst[i]) == x:
            print(i, end=' ')
else:
    print('Отсутствует')

# Вариант 2
# i = 0
# j = lst.count(x)
# if x in lst:
#     while i < j:
#         print(lst.index(x), end=' ')
#         lst[lst.index(x)] = ''
#         i += 1
# else:
#     print("Отсутствует")