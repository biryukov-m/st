import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)(\1+)'
    mo = re.match(pattern, line)
    # print(line)
    # print(mo)
    # print(mo.group(2))
    # print(mo.group(3))
    line = re.sub(pattern, r'\1', line)
    print(line)