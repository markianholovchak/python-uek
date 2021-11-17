with open('numbers.txt', 'r') as f:
    totalSum = 0
    for line in f:
        totalSum+= int(line)

print(totalSum)