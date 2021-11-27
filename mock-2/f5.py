def f5(c):
    lines = 0
    with open('poem.txt') as f:
        for line in f:
            print(line, c in line)
            if c in line.lower():
                lines+=1
    return lines

print(f5("m"))