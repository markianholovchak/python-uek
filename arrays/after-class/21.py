def secondMax(arr):
    secondMax = firstMax = -1
    ln = len(arr)
    for i in range(ln):
        if arr[i] > firstMax:
            secondMax = firstMax
            firstMax = arr[i]
        if arr[i] > secondMax and arr[i] < firstMax:
            secondMax = arr[i]
    return secondMax

testArr = [5,3,9,6,8]
print(secondMax(testArr))