import random
class Termometer():
    def __init__(self):
        self.temperature = 0
        self.isOn = False
    def turnOn(self):
        self.isOn = True
    def turnOff(self):
        self.isOn = False
    def displayTemp(self):
        print(self.temperature, end=" ")
        if self.temperature >= 37.0 and self.temperature < 41.0:
            print("Fever!")
        elif self.temperature >= 41.0:
            print("Critical temperature!!!")
        else:
            print()
    def measure(self):
        if self.isOn:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Turn the termometer on first!")