# Get the height from the user and convert it from cm to m
height = float(input("Enter your height in cm:")) / 100 
weight = float(input("Enter your weight in kg:"))
bmi = weight / height**2
print(f"BMI index: {bmi:.2f}") # Print out BMI rounded to the first decimal position