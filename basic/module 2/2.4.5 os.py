import os.path
print()
print(os.getcwd())
print(type(os.getcwd()))
print(os.listdir())
print()
print(os.path.abspath('2.2.5.py'))

print()
print('os.walk demonstratoin: ')
for cd, d, f in os.walk('..'):
    print('Current dir > ', cd, '\n', 'Dirs > ', d, '\n', 'Files > ', f)
    print()