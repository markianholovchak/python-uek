# with open("countries.txt", 'r') as f:
#     for index,line in enumerate(f):
#         print(f"Line nr {index+1} {line}", end="")


file = open('countries.txt', 'r')
for line in file:
    print(line, end="")
file.close()