numOfPrimes = int(input("How many primes do you want? "))

counter = 0
numberToCheck = 2
outputStr = "Prime numbers: "
while(counter < numOfPrimes):
    """
    Look for prime numbers until enough
     - Check if the checked number is divisible by some other integer between 1 and itself
     - If it is, then it is not a prime number and we move to a number greater by 1
     - If the number is not divisible by any other integer than 1 or itself then append the number
       to the output string and continue checking next number
    """
    checkStart = 2
    checkEnd = numberToCheck
    isPrime = True
    while(checkStart < checkEnd and isPrime == True):
        # Exit the loop if the checked number is divisible by some other integer than 1 or itself
        if(numberToCheck % checkStart == 0):
            isPrime = False
        checkStart += 1
    if isPrime:
        # If we found a prime number then increase the counter and append the number to output string
        counter +=1
        outputStr += f" {numberToCheck}"
    numberToCheck += 1
        
print(outputStr)
        