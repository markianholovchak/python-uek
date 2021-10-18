def calculateLetters(letter, text):
    """
        Check each letter in a string ( converted to lover case )
        if it is equal to the given argument and increase a counter if so
    """
    counter = 0
    for l in text.lower(): 
        if l == letter:
            counter += 1
    return counter

print(calculateLetters("a", "You never get a second chance to make a first impression" ))

tests = [
    {
        "input": {"letter": "a",
                 "text": "You never get a second chance to make a first impression"
                },
        "output": 4
    },
    {
        "input": {"letter": "e",
                 "text": "You never get a second chance to make a first impression"
                },
        "output": 7
    },
    {
        "input": {"letter": "y",
                 "text": "You never get a second chance to make a first impression"
                },
        "output": 1
    },
    {
        "input": {"letter": "c",
                 "text": "You never get a second chance to make a first impression"
                },
        "output": 3
    },
    {
        "input": {"letter": "i",
                 "text": "You never get a second chance to make a first impression"
                },
        "output": 3
    }
]

for index, test in enumerate(tests):
    if calculateLetters(**test["input"]) == test["output"]:
        print(f"Test {index +1} - passed")
    else:
        print(f"Test {index + 1} - failed")
