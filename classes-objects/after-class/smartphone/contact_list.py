class ContactList():
    def __init__(self):
        self.contactList = []
    def addContact(self, contact):
        self.contactList.append(contact)
    def displayContacts(self):
        for contact in self.contactList:
            print(f"{contact.name} {contact.email} {contact.phone}")