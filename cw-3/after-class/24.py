num = int(input("Enter number: "))

mid = num // 2
for i in range(num):
    if i <= mid:
        for j in range(i + 1):
            print("* ", end="")
    else:
        for z in range(num - i):
            print("* ", end="")
    print("")