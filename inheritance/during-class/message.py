class Message():
    def __init__(self, sender, recipient):
        self.message = ''
        self.sender = sender
        self.recipient = recipient
    def set_message(self,message):
        self.message = message[0].upper() + message[1::].lower() + ",bye"
