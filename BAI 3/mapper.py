import sys

# use map side join

cust_name = {}

with open('cust.txt', 'r') as cust_file:
    for line in cust_file:
        line = line.rstrip()
        words = line.split(',')
        cust_id = words[0]
        name = words[1]
        cust_name[cust_id] = name
for line in sys.stdin:
    line =line.rstrip()
    words = line.split(',')
    cust_id = words[2]
    service=words[4]
    if cust_id in cust_name:
        print(f"{service}\t{cust_name[cust_id]}")
    