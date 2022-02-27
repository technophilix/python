# Method Resolution Order


# 1)The first principle is to search for sub class before going for its baseclass.If 
#     class B is inherited from A it will search B first then go to A

# 2) When a class is inherited from multiple class it searches in orderfrom left to right C(A,B)

# 3) will not visit more than once

class A(object):

    def method(self):
        print('A class method')
        super().method()

class B(object):

    def method(self):
        print('B class method')
        super().method()

class C(object):

    def method(self):
        print('C class method')
        super().method()

class X(A,B):
    def method(self):
        print('X class method')
        super().method() 


class Y(B,C):
    def method(self):
        print('Y class method')
        super().method() 

class P(X,Y,C):
    def method(self):
        print('P class method')
        super().method() 

p = P()
p.method()        


# Method Resolution Order
# 1)The first principle is to search for sub class before going for its baseclass.If 
#     class B is inherited from A it will search B first then go to A

# 2) When a class is inherited from multiple class it searches in orderfrom left to right C(A,B)

# 3) will not visit more than once