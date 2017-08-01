import re
import string
st = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfy
r'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
st = re.sub(r"k", 'm', st)
st = re.sub(r"o", 'q', st)
st = re.sub(r"e", 'g', st)

intab = string.ascii_lowercase
outtab = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
s = st.maketrans(intab, outtab)
print(st.translate(s))
st = '''http://www.pythonchallenge.com/pc/def/map.html'''
s = st.maketrans(intab, outtab)
print(st.translate(s))