from message import Message
class Mail(Message):
    def __init__(self, sender, recipient, subject):
        self.subject = subject
        super().__init__(sender, recipient)
    def send(self):
        print("Sending mail...")
        print(f"From: {self.sender}")
        print(f"To: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"To: {self.message}")
        print(f"Mail sent")