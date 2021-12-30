class C():
    def __init__(self, array):
        self.array = array
    def m(self):
        counter = 0
        for i in range(1, len(self.array) - 1):
            if self.array[i - 1] != self.array[i] and self.array[i - 1] == self.array[i + 1]:
                counter += 1
        return counter
    
print(C([True,False,False]).m())
print(C([True,False,True,False]).m())
print(C([True,False,True,True,False,True,False,True,False]).m())
            