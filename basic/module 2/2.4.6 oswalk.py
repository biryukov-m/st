import os.path
scriptdirs = []
for cd, d, f in os.walk('main'):
    for file in f:
        if '.py' in file:
            print('Python scripts found in > ', cd)
            print('and it is:', file)
            scriptdirs.append(cd)
            break
scriptdirs.sort()
with open('scriptdirs.txt', 'w') as w:
    for d in scriptdirs:
        w.write(d)
        w.write('\n')
