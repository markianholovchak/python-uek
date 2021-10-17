num = int(input("How many Fibbonaci'es do you want? "))
a = 0
b = 1
for i in range(num):
    print(f" {a}", end="")
    a, b = b, a+b