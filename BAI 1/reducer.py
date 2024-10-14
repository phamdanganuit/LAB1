import sys

total={}
for line in sys.stdin:
    line=line.rstrip()
    service,price=line.split('\t')
    price=float(price)
    if service in total:
        total[service]+=price
    else:
        total[service]=price

for value in total:
    print(f'{value}\t{total[value]}')
