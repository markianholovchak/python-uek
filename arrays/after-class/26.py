def separateParity(arr):
    separatedArr = []
    for i in arr:
        if i % 2 == 0:
            separatedArr.insert(0, i)
        else:
            separatedArr.append(i)
    return separatedArr

testArr = [5,4,3,2,6,5]
print(separateParity(testArr))