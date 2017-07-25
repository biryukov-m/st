import requests
import re

html = input().strip()
# html = 'http://pastebin.com/raw/7543p0ns'
# html = 'http://pastebin.com/raw/2mie4QYa'
# html = 'https://www.ukr.net/'
pattern = r'''<.*href\s*=\s*['"](?:[\w*-*]*?://)?(\w[_\w.-]*\w\w)(?:[/:\?\w]*)(?:\w*\.?\w*)?['"]'''
res = requests.get(html).text
url = re.findall(pattern, res)
out = []
for u in url:
    if u not in out:
        out.append(u)
out.sort()
for u in out:
    print(u)