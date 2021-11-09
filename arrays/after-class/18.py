def bubblesort(arr):
    ln = len(arr)
    for i in range(ln-1):
        for j in range(0, ln - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]        
    return arr

print(bubblesort([3,4,2,1]))