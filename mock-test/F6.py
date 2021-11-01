import random
def rand(start, end):
    randomNumber = random.randint(start, end)
    while not (randomNumber % 2 == 0 and randomNumber % 3 == 0):
        randomNumber = random.randint(start, end)
    return randomNumber
