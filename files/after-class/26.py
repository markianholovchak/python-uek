import re
msg = "To be, or not to be, that is the question"

print(len(re.findall('\w+', msg)))
