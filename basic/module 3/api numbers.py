import requests

f = open('data.txt', 'r')
for line in f.readlines():
    number = str(line.strip())
    url = 'http://numbersapi.com/{}/math'.format(number)
    params = {
        'json': 'true'
    }
    res = requests.get(url, params)
    # print(res.text)
    res = res.json()
    # print(res)
    print('Interesting' if res['found'] else 'Boring')
