with open('lorem30.txt', 'r') as f:
    for index,line in enumerate(f):
        print(line, end="")
        if((index + 1) % 5 == 0 ):
            input()