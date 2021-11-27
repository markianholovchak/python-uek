class TV():
    def __init__(self):
        self.isOn = False
        self.channel = 1
    def turn_on(self):
        self.isOn = True
    def turn_off(self):
        self.isOn = False
    def show_status(self):
        print(f"TV is: {'on' if self.isOn else 'off'}")
        if(self.isOn):
            print(f"Channel nr {self.channel}")

myTV = TV()
myTV.show_status()
myTV.turn_on()
myTV.show_status()
myTV.turn_off()
myTV.show_status()