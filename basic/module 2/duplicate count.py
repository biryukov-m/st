def duplicate_count(text):
    text = text.lower()
    symbols = {}
    res = 0
    for sym in text:
        if sym not in symbols:
            symbols[sym] = 1
        else:
            symbols[sym] += 1
    for sym, count in symbols.items():
        if count > 1:
            res += 1
    return res
    # Your code goes here

vasa = '1'
print(duplicate_count(vasa))