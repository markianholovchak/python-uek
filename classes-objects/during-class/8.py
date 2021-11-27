class University():
    def __init__(self):
        self.name = 'CUE'
    def print_name(self):
        print(self.name)
    def set_name(self, name):
        self.name = name


newUniversity = University()
newUniversity.print_name()
newUniversity.set_name('MIT')
newUniversity.print_name()
