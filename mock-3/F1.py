class C():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"{self.name[0].upper()}{self.surname[0].upper()}"
    
myObj = C("anna","may")
print(myObj)