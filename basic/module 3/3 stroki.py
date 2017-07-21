s = str(input())
a = str(input())
b = str(input())
c = 0

while a in s:
    if a in b:
        print("Impossible")
        break
    s = s.replace(a, b)
    c += 1
else:
    print(c)