



import requests
from time import sleep


f = '77.222.148.56 - 77.222.148.63'

url = 'http://rest.db.ripe.net/ripe/inetnum/{}.json'.format(f)
res = requests.get(url)
# print(res.text)
sleep(0.5)
print(res.text)
data = res.json()
if 'errormessages' in data.keys():
    print(f, '- не найдено в базе')
    print()
data = data["objects"]["object"][0]["attributes"]["attribute"]
for dic in data:
    if 'inetnum' in dic.values():
        print(dic['value'])
    if 'netname' in dic.values():
        print(dic['value'])
    if 'descr' in dic.values():
        print(dic['value'])
    if 'country' in dic.values():
        print(dic['value'])
print()
# sleep(1)
