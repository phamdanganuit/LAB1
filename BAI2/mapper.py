import sys

cust_name  = {}

#Mapside Join

with open('cust.txt', 'r') as cust_file:
    for line in cust_file:
        line = line.rstrip()
        words = line.split(',')
        cust_id = words[0]
        name=words[1]
        cust_name[cust_id] = name
        
for line in sys.stdin:
    line=line.rstrip()
    words=line.split(',')
    cust_id=words[2]
    price=float(words[3])
    
    if words[4] == 'Outdoor Recreation':
        if cust_id in cust_name:
            print(f"{cust_name[cust_id]}\t{price}")
    