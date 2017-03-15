lst = a = []
while 'end' not in a:
    a = input()
    if 'end' not in a: lst.append(list(map(int, a.split())))
li, lj = len(lst), len(lst[0])
new = [[sum([lst[(i-1) % li][j], lst[(i+1) % li][j], lst[i][(j-1) % lj], lst[i][(j+1) % lj]]) for j in range(lj)] for i in range(li)]
for i in range(li):
    for j in range(lj):
        print(new[i][j], end = ' ')
    print()