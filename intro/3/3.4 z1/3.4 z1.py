inf = open('dataset.txt', 'r')
def unpack(inf, ouf=''):
    zip = inf.readline()
    inf.close()
    i = 0
    digit = []
    raw = ''
    letter = ''
    while i < len(zip):
        if zip[i].isalpha():
            letter = str(zip[i])
        else:
            digit.append(zip[i])
        if i == len(zip)-1:
            times = int(''.join(digit))
            digit = []
            for j in range(times):
                raw += letter
                break
        if zip[i+1].isalpha():
            times = int(''.join(digit))
            digit = []
            for j in range(times):
                raw += letter
        i += 1

    return raw
ouf = open('outdataset.txt', 'w')
raw = ouf.write()