from sms import SMS
from mail import Mail

newSms = SMS("2132133", "12214124")
newSms.set_message("Hello Bob, let's go for a beer on Friday")
newSms.send()
newMail = Mail("me@mail.com", "bob@mail.com", "Friday beer")
newMail.set_message("Hey Bob, I changed my mind: let's go for a whiskey on Friday")
newMail.send()