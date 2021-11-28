from message import Message
class Mail(Message):
    def __init__(self, senderAddress, recipientAddress, subject):
        self.senderAddress = senderAddress
        self.recipientAddress = recipientAddress
        self.subject = subject
        super().__init__()
    def send(self):
        print("Sending mail...")
        print(f"From: {self.senderAddress}")
        print(f"To: {self.recipientAddress}")
        print(f"Subject: {self.subject}")
        print(f"To: {self.message}")