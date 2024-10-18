from collections import defaultdict
import sys

category_totals = defaultdict(float)
category_counts = defaultdict(int)

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) != 2:
        continue
    category, amount = fields
    try:
        amount = float(amount)
    except ValueError:
        continue
    category_totals[category] += amount
    category_counts[category] += 1

if category_counts:
    max_category = max(category_counts, key=category_counts.get)
    max_total = category_totals[max_category]
    print(f"{max_category}\t{max_total}")
else:
    print("No data found")
