import re

def calcAverage(items):
    return sum(items) / len(items)

msg = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
pattern = r"\d{2}"

temps = []
for res in re.findall(pattern, msg):
    temps.append(int(res))
print(f"Average: {calcAverage(temps)}")
