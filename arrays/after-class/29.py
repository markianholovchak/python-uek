def isSubset(arr1, arr2):
    if len(arr1) > len(arr2):
        return False
    for i in arr1:
        if i not in arr2:
            return False
    return True

tests = [
    {
        "arr1": [1,2,3,4],
        "arr2": [1,2,3,4,5,6]
    },
    {
        "arr1": [8,2,1,3,4,5],
        "arr2": [1,3,5,1,8,4,5,2]
    },
    {
        "arr1": [8,2,1,3,4,5,2,1,34,4],
        "arr2": [1,3,5,1,8,4,5,2]
    },
    {
        "arr1": [8,2,1,10],
        "arr2": [1,3,5,1,8,4,5,2]
    },
    {
        "arr1": [],
        "arr2": [1,3,5,1,8,4,5,2]
    },
    {
        "arr1": [],
        "arr2": []
    },
    {
        "arr1": [1],
        "arr2": [2]
    },
    {
        "arr1": [1],
        "arr2": [1]
    }
]
for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    print(isSubset(**test))
    print("-----------------------")
