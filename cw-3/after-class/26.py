PIN = "0805"
attempts = 2
loggedIn = False
while not loggedIn and attempts > 0:
    userInput = input("Enter the PIN code: ")
    if(userInput == PIN):
        print("Successfuly authentificated")
        loggedIn = True
    else:
        print("Incorrect...")
        attempts -= 1
if(attempts == 0):
    print("Sorry, your payment card has been blocked")

# userInput = input("Enter the PIN code: ")
# while(userInput != PIN and attempts > 0):
#     attempts -= 1
#     print("Incorrect...")
#     userInput = input("Enter the PIN code: ")
# if(userInput == PIN):
#     print("Successfuly authentificated")
# else:
#     print("Sorry, your payment card has been blocked")
