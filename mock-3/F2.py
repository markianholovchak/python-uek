class C():
    def __init__(self, text):
        self.text = text
    def m(self):
        for char in self.text:
            counter = 0
            for char2 in self.text:
                if char == char2:
                    counter +=1
            if counter > 1:
                return False
        return True


print(C("red sun").m())
print(C("blue water").m())
print(C("BLUE water").m())