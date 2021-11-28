class Student():
    identifier = 100000
    university = "UEK Krakow"
    def __init__(self, name, surname, fieldOfStudy):
        Student.identifier += 1
        self.name = name
        self.surname = surname
        self.fieldOfStudy = fieldOfStudy
        self.identifier = Student.identifier
    def __str__(self):
        return f"{self.name} {self.surname} ({self.identifier}), {self.fieldOfStudy}, {Student.university}"

studentOne = Student("Mary", "Brown", "Applied Informatics")
studentTwo = Student("John", "Bee", "Finance and Accounting")
studentThree = Student("Rohn", "Jabs", "Applied Mathematics")
print(studentOne)
print(studentTwo)
print(studentThree)