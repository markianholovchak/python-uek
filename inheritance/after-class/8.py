class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.isOn = False
    def turnOn(self):
        self.isOn = True
    def turnOff(self):
        self.isOn = False
    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}\nTurned on: {'Yes' if self.isOn else 'No'}"


iPhone = Phone("Apple", "12 pro", "1200$")
iPhone.turnOn()
xiaomiPhone = Phone("Xiaomi", "Red Mi 5", "125$")
print(iPhone)
iPhone.turnOff()
print(xiaomiPhone)
xiaomiPhone.turnOn()
print(xiaomiPhone)
xiaomiPhone.turnOff()