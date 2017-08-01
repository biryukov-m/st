def accum(s):
    s = '-'.join(c * l for c, l in enumerate(s, 1))
    s = '-'.join(w.capitalize() for w in s.split('-'))
    return s

print(accum('abcd'))