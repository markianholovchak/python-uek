amount = int(input("Enter the amount in PLN: "))
amountCopy = amount

fiveCoins = twoCoins = oneCoins = 0
fiveCoins = amountCopy // 5
amountCopy = amountCopy % 5
if(amountCopy > 0):
    twoCoins = amountCopy // 2
    amountCopy =  amountCopy % 2
oneCoins = amountCopy

print(f"The amount of PLN {amount} in coinss: \n 5 zł - {fiveCoins} \n 2 zł - {twoCoins} \n 1 zł - {oneCoins}")
    
    
# Using loops:

# fiveCoins = twoCoins = oneCoins = 0
# while(amountCopy >= 5):
#     fiveCoins += 1
#     amountCopy -= 5
# while(amountCopy >= 2):
# fiveCoins += 1
# amountCopy -= 2
# oneCoins = amountCopy