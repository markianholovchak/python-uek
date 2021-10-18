def calculateSumOfDigits(number):
    number = abs(number)
    sumOfDigits = 0
    while(number != 0):
        sumOfDigits += number % 10
        number //= 10
    return sumOfDigits

print(calculateSumOfDigits(7182))

tests = [
    {
        "input": {"number": 7182},
        "output": 18
    },
    {
        "input": {"number": 4564},
        "output": 19
    },
    {
    
        "input": {"number": 32523},
        "output": 15
    },
    {
    
        "input": {"number": 947830},
        "output": 31
    },
    {
    
        "input": {"number": 947830213123},
        "output": 43
    },
    {
    
        "input": {"number": 999999999},
        "output": 81
    },
    {
    
        "input": {"number": 9000000000000000},
        "output": 9
    },
    {
    
        "input": {"number": -18932},
        "output": 23
    }
]

for index, test in enumerate(tests):
    if calculateSumOfDigits(**test["input"]) == test["output"]:
        print(f"Test {index +1} - passed")
    else:
        print(f"Test {index + 1} - failed")