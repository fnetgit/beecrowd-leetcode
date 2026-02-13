# Ones

import sys

for line in sys.stdin:
    num = int(line)
    one = 1
    length = 1
    while one % num != 0:
        one = (one * 10 + 1) % num
        length += 1
    print(length)
