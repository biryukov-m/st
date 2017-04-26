with open('dataset.txt', 'r') as i, open('out.txt', 'w') as o:
    tmp = []
    for line in i:
        tmp.append(line)
        print(line)
    tmp.reverse()
    for line in tmp:
        o.write(line)