# There are three types of methods
# 1)Intance method
#     a) accecessor
#     b) mutator
# 2) Class method
# 3) Static method

class Student:
    def setName(self, name1):  #mutator
        self.name=name1
    def getName(self):
        return self.name    
    def setMarks(self, marks1):
        self.marks=marks1
    def getMarks(self): #accessor
        return self.marks 


n = int(input("How meny students"))
i=0

while(i<n):
    s = Student()
    name2 = input('Enter name')
    s.setName(name2)
    marks2 = int(input("enter marks"))
    s.setMarks(marks2)

    print("Hi {}, your marks is {}".format(s.getName(), s.getMarks()))

    i=i+1
    print("----------------------")




