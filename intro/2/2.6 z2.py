digit = 1
times = int(input())
printed = 0
while printed < times:
    i = 0
    while i < digit:
        if printed < times:
            print(digit, end=' ')
        printed += 1
        i += 1
    digit += 1