#####

# Calculation of the area and circumference of a circle

##

# determine radius and PI # 
radius = float(input("Enter the radius of a circle: "))
PI = 3.14

# calculate area #
area = PI*radius**2

# calculate circumference # ]
circumference = 2*PI*radius

# display results # 
print(f"Radius is: {radius}, area is: {area:10.2f}, circumference is: {circumference:10.2f}")
