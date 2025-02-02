class Student:
    def __init__(self):
        self.public_att = "I ama public attibute"
        self._protected_att = "I ama protected attibute"
        self.__private_att = "I ama private attibute"

    # this method is called getter
    def get_private(self):
        return self.__private_att    
    
    # this method is called setter
    def get_private(self, value):
        self.__private_att = value
   
   



s1 = Student()
print(s1.public_att)
print(s1._protected_att)
# print(s1.__private_att)
print(s1.get_private())