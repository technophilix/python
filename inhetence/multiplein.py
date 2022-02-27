"""
class Subclass(Baseclass1, baseclass2, ....):
"""

class Father():
    def height(self):
        print("the height is 6ft")


class Mother:
    def color(self):
        print("the color is brown")



class Child(Father, Mother):
    pass


c = Child()

print("------Inherited Property------")
c.height()
c.color()
