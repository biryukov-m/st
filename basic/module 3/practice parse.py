import requests
import re

seasons = [int(n) for n in range(1, 17)]
series = ['01', '02', '03', '04', '05', '06', '07', '08', '09', 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
print(seasons)
print(series)
urls = []
out = []
for season in seasons:
    for seria in series:
        urls.append('http://familyguy.fox-fan.ru/series.php?id={sea}{ser}'.format(sea=season, ser=seria))

pattern = r'''flashvars.*(rtmp://.*.mp4)'''
with open('familyguy.m3u', 'w') as of:
    of.write('#EXTM3U' + '\n')
for html in urls:
    res = requests.get(html).text
    # print(res)
    urlist = re.findall(pattern, res)
    if len(urlist) > 0:
        for video in urlist:
            # Вывод в файл .
            with open('familyguy.txt', 'a') as of:
                of.write(video + '\n')
            # Вывод в консоль
            print(video)
            # Вывод в M3u
            with open('familyguy.m3u', 'a') as of:
                of.write('#EXTVLCOPT:network-caching=1000' + '\n')
                of.write(video + '\n')