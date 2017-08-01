import requests
import re

res = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html').text
pattern = r'''<!--\s%(.*)-->'''
res = re.findall(pattern, res, re.DOTALL)
res = ''.join(res)


def bylen(l):
    return l[1]
chars = [c for c in res if res.count(c) < 10]
print(chars)