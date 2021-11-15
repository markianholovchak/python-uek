import json

COLUMN_WIDTH = 15
DATE_WIDTH = 10
header_1 = "Date"
header_2 = "Buying rate"
header_3 = "Selling rate"
print("Date"+" "*(COLUMN_WIDTH - len(header_1))+"Buying Rate"+" "*(COLUMN_WIDTH - len(header_2))+"Selling Rate")
print("="*COLUMN_WIDTH * 3)

with open("usdRates.json") as f:
    data = json.load(f)

for rate in data['rates']:
    priceWidth = len(str(rate['bid']))
    print(f"{rate['effectiveDate']} {' '*(COLUMN_WIDTH - DATE_WIDTH)}{rate['bid']}{' '*(COLUMN_WIDTH - priceWidth)}{rate['ask']}") 