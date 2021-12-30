import turtle

class MyTurtle(turtle.Turtle):
    def square(self, sideSize):
        for i in range(4):
            self.forward(sideSize)
            self.left(90)
    def triangle(self, sideSize, angle):
        for i in range(3):
            self.forward(sideSize)
            self.left(180 - angle)
    def arrow(self):
        self.forward(60)
        self.right(90)
        self.forward(15)
        self.left(135)
        self.forward(40)
        self.left(90)
        self.forward(40)
        self.left(135)
        self.forward(15)
        self.right(90)
        self.forward(60)
        self.left(90)
        self.forward(35)
    def semicircle(self, radius):
        self.forward(radius * 2)
        self.left(90)
        self.circle(radius, 180)
    def octagon(self, sideSize):
        for i in range(8):
            self.forward(sideSize)
            self.left(45)
    def cross(self, sideSize):
        for i in range(4):
            self.left(90)
            self.forward(sideSize)
            self.left(90)
            self.forward(sideSize)
            self.right(90)
            self.forward(sideSize)
    def star(self, sideSize, angle):
        self.color("black", "white")
        self.begin_fill()
        for i in range(5):
            self.forward(sideSize)
            self.right(angle)
        self.end_fill()
    
myTurtle = MyTurtle()
# myTurtle.square(100)
# myTurtle.moveDown(100)
# myTurtle.triangle(100, 60)
# myTurtle.moveDown(100
# myTurtle.octagon(25)
# myTurtle.cross(25)
myTurtle.star(100, 144)

turtle.done()