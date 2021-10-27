import mymath

userNum = mymath.read_number()
compNum = mymath.generate_number()

if(userNum == compNum):
    print("You win!")
else:
    print("You lose!")
