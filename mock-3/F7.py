import json
class C():
    def __init__(self):
        with open("mockdata.json") as f:
            self.families = json.load(f)
    def m(self, n1, n2):
        counter = 0
        for family in self.families:
            if int(family["wife"]["age"]) >= n1 and len(family["children"]) >= n2:
                counter += 1
        return counter
    def m2(self, n1):
        familiesToWrite = []
        for family in self.families:
            if len(family["children"]) >= n1:
                familiesToWrite.append(family)
        with open("mockdata1.json", "w") as f:
            json.dump(familiesToWrite,f, indent=2) 

print(C().m(40, 1))
    

        