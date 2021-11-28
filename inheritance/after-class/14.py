class Areas():
    @staticmethod
    def calculateCircle(r):
        return 3.14 * r**2
    @staticmethod
    def calculateRectangle(a,b):
        return a * b
    @staticmethod
    def calculateTriangle(base,height):
        return base*height/2

print(Areas.calculateCircle(3))
print(Areas.calculateRectangle(4,7))
print(Areas.calculateTriangle(6,2))