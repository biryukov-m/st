import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(\w)(\w)(\w*)\b'
    mo = re.match(pattern, line)
    # print(line)
    # print(mo)
    # print(mo.group(2))
    # print(mo.group(3))
    line = re.sub(pattern, r'\2\1\3', line)
    print(line)