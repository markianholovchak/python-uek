import random
with open('randomIntegers.txt', 'w') as f:
    for i in range(1, 51):
        if i == 50:
            f.write(f"{random.randint(100, 999)}")
        else:
            f.write(f"{random.randint(100, 999)}\n")