# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\\'
    if re.search(pattern, line):
        print(line)