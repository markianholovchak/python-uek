def separateByComma(arr):
    return ",".join(str(i) for i in arr)

testArr = [5,4,3,2,6,5]
print(f"Array: {testArr}\nString: {separateByComma(testArr)}")