def sumOfArr(arr):
    suma = 0
    for i in arr:
        suma += i
    return suma
arr = [4,3,7,1,3]
def array2str(arr):
    return " ".join(str(i) for i in arr)
print("Array: "+array2str(arr))
print(f"Sum of values: {sumOfArr(arr)}")
