import random
numToGuess = random.randint(1, 6)
usersGuess = int(input("Guess the number: "))
while(usersGuess != numToGuess):
    print(False)
    usersGuess = int(input("Guess the number: "))
print(True)
    