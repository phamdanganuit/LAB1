#!/usr/bin/env python3
import sys

current_service = None
current_customer = None
current_count = 0
max_count = 0
max_customer = None

customer_dict = {}
with open("cust.txt", "r") as f:
    for line in f:
        cust_id, first_name, last_name, _, _ = line.strip().split(",")
        customer_dict[cust_id] = f"{first_name} {last_name}"

for line in sys.stdin:
    service, customer, count = line.strip().split("\t")
    count = int(count)

    if current_service == service:
        if current_customer == customer:
            current_count += count
        else:
            if current_count > max_count:
                max_count = current_count
                max_customer = current_customer
            current_customer = customer
            current_count = count
    else:
        if current_service:
            if current_count > max_count:
                max_customer = current_customer
            print(f"{current_service}\t{customer_dict[max_customer]}")
        current_service = service
        current_customer = customer
        current_count = count
        max_count = count
        max_customer = customer

if current_service:
    if current_count > max_count:
        max_customer = current_customer
    print(f"{current_service}\t{customer_dict[max_customer]}")
