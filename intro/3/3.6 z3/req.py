inf = open('dataset.txt', 'r')
srcUrl = inf.readline().strip()
croppedSrcUrl = srcUrl.split('/')
baseUrl = ''
for i in range(len(croppedSrcUrl)-1):
    baseUrl += croppedSrcUrl[i]
    baseUrl += '/'
print(srcUrl, ' - Source url')
print(baseUrl, '  -  base url')
import requests
txtFile = 'ijqopwie qjwpoerij qori'
i = 0
while 'we' not in txtFile:
    r = requests.get(srcUrl)
    txtFile = r.text
    srcUrl = baseUrl+txtFile
    i += 1
    print('Цикл - ', i)
    print('Полученная ссылка - ', srcUrl)
    print()
print('Агаааа, попался!', txtFile)