from urllib import request as req
import zipfile
import re

zipurl = 'http://www.pythonchallenge.com/pc/def/channel.zip'
url = req.urlopen(zipurl)
# Filename
name = zipurl[-11:]
# Writing zipurl to filesystem
with open(name, 'wb') as f:
    f.write(url.read())
# Creating zipfile object
zf = zipfile.ZipFile(name)
# Lets see what we have in archive
# [print(file) for file in zf.filelist]
# OK, found readme.txt, reading
read = zf.read('readme.txt')
print(read)
# Starting from 90052, reading
read = zf.read('90052.txt')
print(read)
# That's the trick with the nothings
# Starting to search from 90052.txt
nothing = '90052'
# Reading text in all files consecutive
# STEP 2  Com for collecting comments
com = []
while True:
    # Extracting file with dynamic path
    read = zf.read(nothing+'.txt')
    # Converting byte obj to string
    read = read.decode('ascii')
    # STEP 2 Collecting comments
    com.append(zf.getinfo(nothing+'.txt').comment.decode('ascii'))
    # With regex finding digits, when pattern coincided
    try:
        nothing = re.findall('Next nothing is (\d+)', read)[0]
    except:
        break
# STEP 2
print(''.join(com))
