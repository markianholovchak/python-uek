SPEED_LIMIT = 130
currentSpeed = int(input("Enter your current speed: "))
if(currentSpeed > SPEED_LIMIT):
    """
    Calculate the exceeding speed and print it out
    """
    exceeding = currentSpeed - SPEED_LIMIT
    print(f"You are exceeding a speed limit which is 130km/h by {exceeding}km/h")
else:
    print("You are a good driver! :)")