height = int(input("Insert height of a tree: "))
for i in range(height):
    for j in range(height * 2 - 1):
        if (i+j) < height-1 or (j-i) > height-1:
            print(" ", end="")
        else:
            print("*", end="")
    print("")


for i in range(5):
    if i in range(2, 4):
        print(i)
