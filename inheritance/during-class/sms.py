from message import Message
class SMS(Message):
    def __init__(self, senderNumber, recipientNumber):
        self.senderNumber = senderNumber
        self.recipientNumber = recipientNumber
        super().__init__()
    def send(self):
        print("Sending sms...")
        print(f"From: {self.senderNumber}")
        print(f"To: {self.recipientNumber}")
        print(f"To: {self.message}")