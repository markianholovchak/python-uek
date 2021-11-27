import csv
def f6(g, n1, n2):
    counter = 0
    with open("people.csv") as f:
        people = csv.DictReader(f)
    for human in people:
        if human['gender'] == g and int(human['height']) in range(n1, n2+1):
            counter +=1
    return counter
print(f6("Female",160,180))