#!/usr/bin/env python3
import sys

customer_dict = {}
with open("cust.txt", "r") as f:
    for line in f:
        cust_id, first_name, last_name, _, _ = line.strip().split(",")
        customer_dict[cust_id] = f"{first_name} {last_name}"

for line in sys.stdin:
    if line.startswith("transaction_id"):
        continue

    fields = line.strip().split(",")
    if len(fields) >= 6:
        cust_id = fields[2]
        service_type = fields[4]

        if cust_id in customer_dict:
            print(f"{service_type}\t{cust_id}\t1")
