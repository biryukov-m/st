# V1


import sys
import re
pattern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    b = re.findall(pattern, line)
    if len(b) > 1:
        print(line)


# V2

import sys, re
for line in sys.stdin:
    pattern = r"cat.*cat"
    line = line.rstrip()
    result = re.findall(pattern, line)
    if result:
        print(line)