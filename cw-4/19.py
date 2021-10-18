def isInRange(num, rangeStart, rangeEnd):
    return num >= rangeStart and num <= rangeEnd

tests = [
    {
        "input": {"num": 5,
                  "rangeStart": 10,
                  "rangeEnd": 20,
                  },
        "output": False
    },
    {
        "input": {"num": 7,
                  "rangeStart": 3,
                  "rangeEnd": 20,
                  },
        "output": True
    },
    {
        "input": {"num": 0,
                  "rangeStart": 0,
                  "rangeEnd": 0,
                  },
        "output": True
    },
    {
        "input": {"num": 3,
                  "rangeStart": 1,
                  "rangeEnd": 1,
                  },
        "output": False
    },
     {
        "input": {"num": 568,
                  "rangeStart": 1,
                  "rangeEnd": 235325,
                  },
        "output": True
    },
   
]

for index, test in enumerate(tests):
    if isInRange(**test["input"]) == test["output"]:
        print(f"Test {index +1} - passed")
    else:
        print(f"Test {index + 1} - failed")