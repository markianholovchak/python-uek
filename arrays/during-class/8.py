arr = [-15, 8, -31, 47, -2, 19]
print(max(arr), " Max ",min(arr), " Min " )
def findMaxAndMin(array):
    minim = maxim = array[0]
    for i in array:
        if i > maxim:
            maxim = i
        if i < minim:
            minim = i
    return [f"Max: {maxim}", f"Min: {minim}"]
print(*findMaxAndMin(arr))
