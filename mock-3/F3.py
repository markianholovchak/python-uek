class C():
    def __init__(self, names):
        self.names = names
    def m(self):
        for name in self.names:
            counter = 0
            for name2 in self.names:
                if name.lower().strip() == name2.lower().strip():
                    counter += 1
            if counter > 1:
                return True
        return False
    
print(C(["Anna"]).m())
print(C(["Anna","John"]).m())
print(C(["Anna","John","Anna"]).m())
print(C(["ANNA","John","Anna"]).m())