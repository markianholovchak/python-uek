from helper import array2str
def longestName(arr):
    maxLen = 0
    longName = ""
    for name in arr:
        if len(name) > maxLen:
            maxLen = len(name)
            longName = name
    return longName

testArr = ["Genowena","Onufry", "Celestyna","Alojzy","Pankracy"]
print(f"Names: {array2str(testArr)}\nLongest name: {longestName(testArr)}")