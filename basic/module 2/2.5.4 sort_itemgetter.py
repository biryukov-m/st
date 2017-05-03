x = [
    ('Guido', 'Van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

import operator as op
x.sort(key=op.itemgetter(-1))
print(x)