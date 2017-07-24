import requests
import re

# html = input().strip()
html = 'https://www.ukr.net/'
pattern = r'<a[^>]*?href="(https?.^/*?)"[^>]*?>'
res = requests.get(html).text
urls = re.findall(pattern, res)
urls.sort()
for url in urls:
    print(url)