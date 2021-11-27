def f2(a1, a2):
    counter = 0
    for num in a1:
        if len(str(num)) == 2:
            counter += 1
    for num in a2:
        if len(str(num)) == 2:
            counter -= 1

    return counter == 0

print(f2([23,7,16,34], [1,18,79,20,6,111]))