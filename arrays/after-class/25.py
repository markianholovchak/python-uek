from helper import findMin, findMax

def minmax(arr):
    return [findMin(arr), findMax(arr)]

testArr = [4,2,8,4,7,9,5]
print(minmax(testArr))