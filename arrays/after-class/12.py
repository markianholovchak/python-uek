from helper import array2str
def reverse(arr):
    reverseArr = []
    for i in range(len(arr)-1, -1, -1):
        reverseArr.append(arr[i])
    return reverseArr

# def reverse(arr):
#     return arr[::-1]

testArr = [15,8,31,47,2,19]
print(f'existed array: {array2str(testArr)}\nreverse array: {array2str(reverse(testArr))}')