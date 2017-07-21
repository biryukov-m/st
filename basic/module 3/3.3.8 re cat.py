import re
import sys

for line in sys.stdin:
    pattern = r".*\bcat\b.*"
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)