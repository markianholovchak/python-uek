import math
from helper import array2str
def median(arr):
    return arr[math.floor(len(arr)/2)]

tests = [
    {
        "arr": [1,0,9,4,6]
    },
    {
        "arr": [6,8,3,1,0,5,7]
    }
]
for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    print(f"Array: {array2str(**test)}\nMedian: {median(**test)}")
    print("-----------------------")