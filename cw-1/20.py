height = int(input("Enter your height in cm:")) / 100
weight = int(input("Enter your weight in kg:"))
bmi = weight / height**2
print(f"BMI index: {bmi:10.1f}") # Print out BMI rounded to the first decimal position