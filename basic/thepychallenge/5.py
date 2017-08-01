import pickle

with open('banner.p', 'rb') as d:
    obj = pickle.load(d)

for o in obj:
    print()
    for b in o:
        print(b[0]*b[1], end='')