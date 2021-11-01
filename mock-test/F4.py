def coins(price):
    fiveCoins = twoCoins = oneCoins = 0
    while(price >= 5):
        fiveCoins +=1
        price -= 5
    while(price >= 2):
        twoCoins += 1
        price -=2
    oneCoins = price
    return fiveCoins + twoCoins + oneCoins
