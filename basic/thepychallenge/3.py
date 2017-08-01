import requests
import re

res = requests.get('http://www.pythonchallenge.com/pc/def/equality.html').text
pattern = r'''[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'''
res = re.findall(pattern, res, re.DOTALL)
res = ''.join(res)
print(res)

# chars = [c for c in res if res.count(c) < 10]
# print(chars)