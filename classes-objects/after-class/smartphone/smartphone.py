from contact import Contact
from contact_list import ContactList

john = Contact("John Brown", "brown@onet.pl", "555234000")
anna = Contact("Anna May", "am@o2.pl", "232000199")
george = Contact("George Small", "smallg@google.pl", "222999100")
paola = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

myContactList = ContactList()
myContactList.addContact(john)
myContactList.addContact(anna)
myContactList.addContact(george)
myContactList.addContact(paola)
myContactList.displayContacts()