with open('lorem.txt', "r") as f:
    with open('copylines.txt', "w") as f2:
        for line in f:
            f2.write(line)


