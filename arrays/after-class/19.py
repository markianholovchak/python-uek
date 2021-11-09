def getUnique(arr):
    uniqueValues = []
    checked = []
    for index,num in enumerate(arr):
        if num not in checked and num not in arr[index+1:]:
            uniqueValues.append(num)
        if num not in checked:
            checked.append(num)
    return uniqueValues



testArr = [2,3,2,5,8,1,9,8]
print(getUnique(testArr))