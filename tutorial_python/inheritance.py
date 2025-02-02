class A:
    a=1
    b=2
    def m1(self):
        print(self.a)
        print(self.b)

class B(A):
    c=3
    def m2(self):
        print(self.c)

b = B()
b.m1()