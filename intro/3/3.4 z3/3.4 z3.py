inf = open('dataset.txt', 'r')
srcInfo = []
with open('dataset.txt') as inf:
    for line in inf:
        srcInfo += [line.strip().split(sep=';')]
allMath, allPhys, allRuss = [], [], []
for el in srcInfo:
    math = int(el[1])
    allMath += [math]
    phys = int(el[2])
    allPhys += [phys]
    russ = int(el[3])
    allRuss += [russ]
    arith = (math+phys+russ)/(len(el)-1)
    print(arith)
print(sum(allMath)/len(allMath), sum(allPhys)/len(allPhys), sum(allRuss)/len(allRuss))