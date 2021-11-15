sumOfNumbers = 0
enteredNum = counter = -1
while enteredNum != 0:
    enteredNum = int(input("Enter number: "))
    sumOfNumbers += enteredNum
    counter += 1
    
mean = sumOfNumbers / counter
print(f"RESULT: Quantity={counter}, Sum={sumOfNumbers}, Mean={mean}")
