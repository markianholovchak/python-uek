import re
import stack
def evaluateInput(inp):
    numPattern = r"^\d+$"
    signPattern = r"^\+|-|=|\*|/$"
    if re.match(numPattern, inp):
        stack.push(int(inp))
    elif re.match(signPattern, inp):
        if inp == "=":
            result = stack.pop()
            if result:
                print(result)
            else:
                print("Nothing to display yet")
        else:
            secondArg = stack.pop()
            firstArg = stack.pop()
            if firstArg and secondArg:
                stack.push(eval(f"{firstArg}{inp}{secondArg}"))
            else:
                print("Not enough operands")
    else:
        print("Invalid input")


userInput = input("Enter a value (write q to exit a program): ")
while(userInput != "q"):
    evaluateInput(userInput)
    userInput = input("Enter a value (write q to exit a program): ")
