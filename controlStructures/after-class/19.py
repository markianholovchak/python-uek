dogAge = int(input("Enter your dog's age: "))
humanAge = 0
if(dogAge > 2):
    humanAge = (dogAge - 2)*4 + 2*10.5
else:
    humanAge = dogAge * 10.5
print(f"The dog's age in dog's years is {humanAge} years")