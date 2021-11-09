def printFormatted(arr):
    ln = len(arr)
    print("-"*(ln*5 + 1))
    print("|", end="")
    for i in arr:
        digits = len(str(i))
        print(" "*(4 - digits) + str(i) + "|", end="")
    print()
    print("-"*(ln*5 + 1))

testArr = [1,23,5,382,1,17,4,906]
printFormatted(testArr)