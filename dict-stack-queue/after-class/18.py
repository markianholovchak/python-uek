import stack

def converter(num):
    while(num > 0):
        stack.push(str(num % 2))
        num //= 2
    poppedVal = stack.pop()
    convertedNum = ""
    while(poppedVal != None):
        convertedNum += poppedVal
        poppedVal = stack.pop()
    return convertedNum

numToConvert = int(input("Enter number to convert to binary: "))
print(converter(numToConvert))