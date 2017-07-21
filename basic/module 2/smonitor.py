import requests
from time import sleep

template = 'Response from {0.url} with code {0.status_code}.'
prevcode = 0
while True:
    res = requests.get('https://2ch.hk/')
    nowcode = res.status_code
    if prevcode == 0:
        print('Starting to monitor {0.url} with code {0.status_code}'.format(res))
    elif prevcode != nowcode:
        print('Code changed from {} to {}'.format(prevcode, nowcode))
    prevcode = nowcode
    print(template.format(res))
    sleep(3)