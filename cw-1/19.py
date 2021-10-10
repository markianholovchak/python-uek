a = int(input("Enter first side of the triangle: "))
b = int(input("Enter second side of the triangle: "))
c = int(input("Enter third side of the triangle: "))
p = (a+b+c)/ 2
area = (p * (p-a) * (p-b) * (p-c))**0.5
print(f"The area of the triangle is: {area}")