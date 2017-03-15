raw = str(input())
t = 0
cnt = 1
while t < len(raw)-1:
    if raw[t] == raw[t+1]:
        cnt += 1
    else:
        print(raw[t], cnt, end='', sep='')
        cnt = 1
    t += 1
print(raw[t], cnt, end='', sep='')

