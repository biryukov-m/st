s = input()
t = input()
# s = 'asdf'
if t in s:
    ind = 0
    cnt = 0
    while cnt != -1:
        cnt = s.find(t)
        s = s[cnt+1:]
        if cnt >= 0:
            ind += 1
print(ind)