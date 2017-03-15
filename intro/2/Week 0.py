# # поиск минимума
# a = [int(i) for i in input().split()]
# m = a[0]
# for i in range(len(a)):
#     if m>a[i]:
#         m = a[i]
# print(m)

# поиск минимума v2
a = [int(i) for i in input().split()]
m = a[0]
for i in a:
    if i < m:
        m = i
print(m)