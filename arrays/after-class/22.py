# def minMaxDiff(arr):
#     return max(arr) - min(arr)
from helper import findMax,findMin

def minMaxDiff(arr):
    return findMax(arr) - findMin(arr)


testArr = [5,1,9,6,1]
print(minMaxDiff(testArr))