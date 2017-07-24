import requests
from time import sleep

template = 'Response from {0.url} with code {0.status_code}.'
while True:
    res = requests.get('https://public.nazk.gov.ua')
    print(template.format(res))
    sleep(10)
