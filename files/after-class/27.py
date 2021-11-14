import re
with open('lorem.txt', 'r') as f:
    content = f.read()
    for match in re.findall(r'\w{6,}', content):
        assert(len(match) >= 6)
        print(match)