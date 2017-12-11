def disemvowel(string):
    em = 'eyuioa'
    ret = ''
    for l in string.lower():
        if l not in em:
            ret += l
    return ret

def emw(char):
    em = 'eyuioa'
    return char in em

print(emw('q'))

ss = 'This website is for losers LOL!'

print(disemvowel(ss))
"N ffns bt,\nr wrtng s mng th wrst 'v vr rd"
"N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"