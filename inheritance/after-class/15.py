class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, another):
        if self.x == another.x and self.y == another.y:
            return True
        return False

pointOne = Point(1, 5)
pointTwo = Point(1, 1)
if(pointOne == pointTwo):
    print("Distance is 0")
else:
    print(round(((pointOne.x - pointTwo.x)**2 + (pointOne.y - pointTwo.y)**2)**(1/2), 2))