class University():
    def __init__(self):
        self.name = 'CUE'
        self.fullName = "Cracow University of Economics"
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name
    def print_fullname(self):
        print(self.fullName)
    def set_fullname(self, fullName):
        self.fullName = fullName

newUni = University()
newUni.print_name()
newUni.print_fullname()
newUni.set_name("MIT")
newUni.set_fullname("Massachusetts Institute of Technology")
newUni.print_name()
newUni.print_fullname()
