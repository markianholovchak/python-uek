class C():
    def __init__(self, text):
        self.text = text
    def m1(self):
        counterChars = {}
        for char in self.text:
            if char in counterChars.keys():
                counterChars[char] += 1
            else:
                counterChars[char] = 1
        return counterChars
    def m2(self, c1):
        countedChars = self.m1()
        countedPassedChars = {}
        for char in c1:
            countedPassedChars[char] = countedChars[char]
        return countedPassedChars
        
        
print(C("my moon").m1())
print(C("my moon").m2("mn"))