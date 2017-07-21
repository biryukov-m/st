import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(\w+)\1\b'
    if re.search(pattern, line):
        print(line)