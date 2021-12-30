class C():
    def __init__(self, number):
        self.number = number
    def m(self):
        numberInDecimal = 0
        for index, num in enumerate(self.number["value"]):
            if int(num) >= int(self.number["system"]):
                return -1
            numberInDecimal += int(num)*int(self.number["system"])**(len(self.number["value"])-index-1)
        return numberInDecimal
    
print(C({"system":"2", "value":"101"}).m())
print(C({"system":"8", "value":"70281"}).m())
            
        