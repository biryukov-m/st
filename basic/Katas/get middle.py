def get_middle(s):
    i = len(s)
    return s[i//2] if i % 2 != 0 else s[(i//2)-1]+s[i//2]

print(get_middle('F'))
