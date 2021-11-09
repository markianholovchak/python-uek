import random
def rand_elem(arr):
    if arr == []:
        return "Invalid input"
    return random.choice(arr)

tests = [
    {
        "arr": [1,2,3,4],
    },
    {
        "arr": [8,2,1,3,4,5],
    },
    {
        "arr": [8,2,1,3,4,5,2,1,34,4],
    },
    {
        "arr": [8,2,1,10],
    },
    {
        "arr": [],
    },
    {
        "arr": [],
    },
    {
        "arr": [1],
    },
    {
        "arr": [1],
    }
]
for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    print(rand_elem(**test))
    print("-----------------------")
