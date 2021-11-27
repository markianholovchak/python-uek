class TV():
    def __init__(self):
        self.isOn = False
        self.channel = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.isOn = True
    def turn_off(self):
        self.isOn = False
    def show_status(self):
        print("-----------------------")
        print(f"TV is: {'on' if self.isOn else 'off'}")
        if(self.isOn):
            print(f"Channel nr {self.channel} - {self.channels[self.channel - 1] if self.channel < len(self.channels) else ''}")
            print(f"Current volume: {self.volume}")
        print("-----------------------")
    def setChannel(self, channel):
        self.channel = channel
    def setChannels(self, channelsList):
        self.channels = channelsList
    def displayChannels(self):
        print(f"Avaliable channels: {','.join(self.channels)} ")
    def increaseVolume(self):
       if self.volume < 10:
            self.volume +=1
    def decreaseVolume(self):
        if self.volume  > 0:
            self.volume -=1

myTV = TV()
myTV.turn_on()
myTV.show_status()
myTV.increaseVolume()
myTV.show_status()
myTV.increaseVolume()
myTV.show_status()
myTV.increaseVolume()
myTV.show_status()
myTV.decreaseVolume()
myTV.show_status()
myTV.decreaseVolume()
myTV.show_status()
myTV.turn_off()