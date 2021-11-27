class TV():
    def __init__(self):
        self.isOn = False
        self.channel = 1
        self.channels = []
    def turn_on(self):
        self.isOn = True
    def turn_off(self):
        self.isOn = False
    def show_status(self):
        print(f"TV is: {'on' if self.isOn else 'off'}")
        if(self.isOn):
            print(f"Channel nr {self.channel}")
    def setChannel(self, channel):
        self.channel = channel
    def setChannels(self, channelsList):
        self.channels = channelsList
    def displayChannels(self):
        print(f"Avaliable channels: {','.join(self.channels)} ")

myTV = TV()
myTV.show_status()
myTV.turn_on()
myTV.show_status()
myTV.displayChannels()
myTV.setChannels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
myTV.displayChannels()
myTV.show_status()
myTV.turn_off()