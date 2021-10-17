x = int(input("Enter x: "))
y = int(input("Enter y: "))
point = f"P({x},{y})"
position = ""
if x == 0 and y == 0:
    position = "position (0,0)"
elif x > 0 and y > 0:
    position = "first quadrant"
elif x < 0 and y > 0:
    position = "second quadrant"
elif x < 0 and y < 0:
    position = "third quadrant"
elif x > 0 and y < 0:
    position = "fourth quadrant"
    
print(f"Point {point} is in the {position} of the coordinate system")