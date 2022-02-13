
class Student:
    #constructor
    def __init__(self, n="", m=0):
        self.name=n
        self.marks= m
        

    def print_student(self):
        print("Hi {}, your marks is {}".format(self.name, self.marks))


stud = Student()
stud.print_student()

stud2 = Student("John", 65)
stud2.print_student()
