
class Student:

# unnecessary declaration
    name = ''
    roll = ''

    #constructor
    def __init__(self):
        self.name = 'Agniswar'
        self.roll = '00001'

    def print_student(self, n, r):
        self.name = n
        self.roll = r
        print("Roll of {} is {}".format(self.name, self.roll))


stud = Student()

stud.print_student()
stud.print_student('John', '000101')