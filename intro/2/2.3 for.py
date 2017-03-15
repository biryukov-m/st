a, b = (int(i) for i in input().split())
while a % 3 != 0:
    a += 1
s = 0
cnt = 0
for i in range(a, b+1, 3):
    s += i
    cnt += 1
print(s/cnt)