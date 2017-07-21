import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b[aA]+\b'
    line = re.sub(pattern, 'argh', line, count=1)
    print(line)
