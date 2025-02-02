class Sample:
    x = 10 # static or class variable


    @classmethod   
    def modify(self):
        self.x += 1


s1 = Sample()
s2 = Sample()

print("print x in sample s1", s1.x)
print("print x in sample s2", s2.x)

s1.modify()

print("print x in sample s1", s1.x)
print("print x in sample s2", s2.x)