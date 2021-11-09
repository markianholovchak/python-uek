def countGreater(num, arr):
    counter = 0
    for i in arr:
        if i > num:
            counter +=1
    return counter

testArr = [3,4,1,6,3,8,4,1]
numberToCheck = int(input("Enter the number: "))
print(f"There are {countGreater(numberToCheck, testArr)} greater elements from {numberToCheck}")