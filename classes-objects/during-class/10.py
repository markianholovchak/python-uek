class TV():
    def __init__(self):
        self.isOn = False
    def turn_on(self):
        self.isOn = True
    def turn_off(self):
        self.isOn = False
    def show_status(self):
        print(self.isOn)


myTV = TV()
myTV.show_status()
myTV.turn_on()
myTV.show_status()
myTV.turn_off()
myTV.show_status()