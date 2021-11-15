a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(a):
    for j in range(b):
        if (i != 0 and i != a-1) and (j != 0 and j != b-1 ):
            print(" ", end="")
        else:
            print("*", end="")
    print("")