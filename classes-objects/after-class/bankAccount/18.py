from bankAccount import bankAccount

myAccount = bankAccount("12 3456 5555 9090 1111 0000 7722")
myAccount.showStatus()
myAccount.deposit(25.30)
myAccount.showStatus()
myAccount.withdraw(31.70)
myAccount.showStatus()
myAccount.withdraw(14)
myAccount.showStatus()

