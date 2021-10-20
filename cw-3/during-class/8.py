LEGAL_AGE = 18
firstPersonAge = int(input("Enter the first's person's age: "))
secondPersonAge = int(input("Enter the second's person's age: "))
if(firstPersonAge >= LEGAL_AGE and secondPersonAge >= LEGAL_AGE):
    print("These people are adults! ")
else:
    print(f"Either one of these people is underage or they are both under {LEGAL_AGE}")