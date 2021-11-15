num = int(input("Enter number: "))

mid = num // 2
for i in range(num):
    if i <= mid:
            print("* "*(i+1))
    else:
            print("* "*(num-i))
    