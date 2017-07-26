import requests
import re

# html = input().strip()
html = 'https://www.ukr.net/'
pattern = r'''<a.*href\s*=\s*['"](?:[a-zA-Z]{3,5}://)?(\w[_\w.-]*)(?:.*)['"]'''
res = requests.get(html).text
url = re.findall(pattern, res)
# url = re.match(pattern,res)
print(url)
out = []
for u in url:
    if u not in out:
        out.append(u.strip())
out.sort()
for u in out:
    print(u)
    pass
#
# # Сверка выхода с ответом
# out = set(out)
# pb = open('s.txt', 'r')
# inurls = []
# for line in pb.readlines():
#     inurls.append(line.strip('\n'))
# inurls = set(inurls)
# print(inurls.symmetric_difference(out))