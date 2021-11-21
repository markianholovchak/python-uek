import re
msg = "To be, or not to be, that is the question"
pattern = r'\w+'
print(len(re.findall(pattern, msg)))
