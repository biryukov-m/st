import requests
import re

# First nothing was 12435
nothing = '12345'
# Then we got responce with text 16044, asked to
nothing = str(16044/2)
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
res = requests.get(url+nothing).text
while True:
    nothing = re.findall(r"and the next nothing is (\d+)", res)[0]
    res = requests.get(url+nothing).text
    print(res)
