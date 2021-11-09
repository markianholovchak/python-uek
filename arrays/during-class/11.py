from helper import array2str
def compare(arr1,arr2):
    if(len(arr1) != len(arr2)):
        return False
    for index,item in enumerate(arr1):
        if item != arr2[index]:
            return False
    return True

tests = [
    [
        ["water","book","sky"],
        ["water","book","sky"]
    ],
    [
        [True,False],
        [True,False,True]
    ],
    [
        [5,3,1],
        [5,3,1]
    ],
    [
        [3,2,1],
        [3,2]
    ],

]

for index,test in enumerate(tests):
    print(f"Test nr: {index}")
    message = "are not"
    if(compare(*test)):
        message = "are"
    print(f"Array 1: {array2str(test[0])} \nArray 2: {array2str(test[1])} \nComparison: arrays {message} the same")
    print("----------------------------------------")
    
