class bankAccount():
    def __init__(self, accountNumber):
        self.accountNumber = accountNumber
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -=amount
    def showStatus(self):
        print(f"Bank Account No: {self.accountNumber}")
        print(f"Balance: PLN {self.balance}")