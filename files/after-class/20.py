with open('integers.txt', 'w') as f:
    for i in range(1, 51):
        if i == 50:
            f.write(f"{i}")
        else:
            f.write(f"{i}\n")
            