def array2str(arr):
    return " ".join(str(i) for i in arr)

def findMax(arr):
    arrMax = arr[0]
    for i in arr:
        if i > arrMax:
            arrMax = i
    return arrMax

def findMin(arr):
    arrMin = arr[0]
    for i in arr:
        if i < arrMin:
            arrMin = i
    return arrMin