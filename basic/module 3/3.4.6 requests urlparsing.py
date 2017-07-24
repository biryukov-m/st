import requests
import re

urla = input()
urlb = input()
pattern = r'.*href="(.*)">.*'
resa = requests.get(urla).text
urlsa = re.findall(pattern, resa)
check = False
for url in urlsa:
    if check:
        break
    resc = requests.get(url).text
    urlsc = re.findall(pattern, resc)
    for urlc in urlsc:
        if urlc == urlb:
            check = True
            break
print('Yes' if check else 'No')
