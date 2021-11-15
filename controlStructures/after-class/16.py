firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))
if(firstNum < secondNum):
    """
    If first number is lower than the second than display it first
    """
    print(f"{firstNum} {secondNum}")
else:
    """
    In other case first number is greater than the second or equal to it
    """
    print(f"{secondNum} {firstNum}")