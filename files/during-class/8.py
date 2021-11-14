with open("countries.txt", 'r') as f:
    for index,line in enumerate(f):
        print(f"Line nr {index+1} {line}", end="")