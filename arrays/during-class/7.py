# def calcEvenAndOdd(arr):
#     evens = odds = 0
#     for i in arr:
#         if(i % 2 == 0):
#             evens +=1
#         else:
#             odds += 1
#     return [f"{evens} even", f"{odds} odd"]

# print(*calcEvenAndOdd([1,3,2,4,5]))

testArr = [1,3,2,4,5]
evens = odds = 0
for i in testArr:
    if(i % 2 == 0):
        evens +=1
    else:
        odds += 1
print(evens, odds)