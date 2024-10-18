

import sys
for line in sys.stdin:
    line=line.rstrip()
    words = line.split(',')
    service=words[4]
    price=words[3]
    price=float(price)
    print (f"{service}\t{price}")
    