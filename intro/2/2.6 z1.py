su, out = 0, 0
while True:
    a = int(input())
    su += a
    out += a**2
    if su == 0:
        print(su)
        break