import sys

cust_cout={}
current_service= None
for line in sys.stdin:
    line = line.rstrip()
    service,cust_name=line.split('\t')
    if current_service != service:
        if current_service is not None:
            current_service = service
            prin