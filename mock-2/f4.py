def f4(d):
    suma = 0
    for value in d.values():
        for num in value:
            if num in range(5,11):
                suma += num
    return suma

print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))