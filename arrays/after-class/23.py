import math
from helper import array2str
def median(arr):
    arr.sort()
    if(len(arr) % 2 == 0):
        return (arr[len(arr)// 2 - 1] + arr[len(arr) // 2]) / 2
    return arr[len(arr)//2]

tests = [
    {
        "arr": [1,0,9,4,6] 
    },
    {
        "arr": [6,8,3,1,0,5,7]
    },
    {
        "arr": [6,8,3,1,0,5]
    }
]
for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    print(f"Array: {array2str(**test)}\nMedian: {median(**test)}")
    print("-----------------------")