#Instance variable
#Class variable or Static varible

class Sample:
    def __init__(self):
        self.x=10

    def modify(self):
        self.x+=1


s1 = Sample()
s2 = Sample()

#for example, dont do this i.e dont use class varible outside this class. reference: accessor and mutator
print("x in s1", s1.x)
print("x in s2", s2.x)

s1.modify()
print("x in s1", s1.x)
print("x in s2", s2.x)