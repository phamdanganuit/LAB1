import sys 
total={}
for line in sys.stdin:
    line= line.rstrip()
    name,price=line.split('\t')
    if name in total:
        total[name]+=float(price)
    else:
        total[name]=float(price)
for value in total:
    print(f'{value}\t{total[value]}')