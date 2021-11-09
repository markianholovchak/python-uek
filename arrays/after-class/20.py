from helper import array2str
def occurs(num, arr):
    return num in arr

tests = [
    {
        "num": 23,
        "arr": [15,38,7,23,14]
    },
    {
        "num": 8,
        "arr": [15,38,7,23,14]
    }
]

for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    msg = "does not appear"
    if(occurs(**test)):
        msg = "appears"
    print(f"Number: {test['num']}\nArray: {array2str(test['arr'])}\nResult: number {test['num']} {msg} in the array")
    print("-----------------------")