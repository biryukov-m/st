# http://ninjaside.info/blog/ru/funkcii-map-i-zip-i-lambda-python/

from urllib import request as req
import zipfile
import re

import requests
zipurl = 'http://www.pythonchallenge.com/pc/def/channel.zip'
url = req.urlopen(zipurl)
name = zipurl[-11:]

with open(name, 'wb') as f:
    f.write(url.read())

zf = zipfile.ZipFile(name)
name += '/99905.txt'
print(name)
zi = zipfile.ZipInfo(name)
print(zi.comment)
# print(zf.namelist())
# print(zf.getinfo('29.txt'))
# zf.extractall('./zfiles')
# infl = list(zf.infolist())
# for i in infl:
    # print(type(i))
    # if 'com' in i:
    #     print(i)
# print(type(list(zf.infolist())))
# for member in zf.namelist():
#     pr = zf.getinfo(member)
#     pr = zf.comment
#     print(pr)

# path = ('./zfiles/')
# nothing = '90052'
# ext = '.txt'
# b = []
# comments = []
# while True:
#     try:
#         with open(path+nothing+ext, 'r') as txt:
#             line = txt.readline()
#             print(line)
#             nothing = re.findall('nothing is (\d+)', line)[0]
#             b.append(nothing+ext)
#     except:
#         break
# print(len(zf.namelist()))
# a = zf.namelist()
# print(len(b))
# print(set.difference(set(a), set(b)))