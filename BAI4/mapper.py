import sys

for line in sys.stdin:
    fields = line.strip().split(",")
    if len(fields) < 5:
        continue
    category = fields[4]
    try:
        amount = float(fields[3])
    except ValueError:
        continue
    print(f"{category}\t{amount}")
