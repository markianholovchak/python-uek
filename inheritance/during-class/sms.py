from message import Message
class SMS(Message):
    def __init__(self, sender, recipient):
        super().__init__(sender, recipient)
    def send(self):
        print("Sending sms...")
        print(f"From: {self.sender}")
        print(f"To: {self.recipient}")
        print(f"To: {self.message}")
        print(f"Sms sent")