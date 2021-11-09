def arrDifference(arr1, arr2):
    difference = []
    checked = []
    for i in arr1:
        if i in checked:
            continue
        if i not in arr2:
            difference.append(i)
        checked.append(i)    
    return difference

testArr1 = [4,36,12,28,9,44,5]
testArr2 = [5,1,36]
print(arrDifference(testArr1, testArr2))
