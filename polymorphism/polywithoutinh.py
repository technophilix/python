#polymorphism without inheritence

class Birds:
    def intro(self):
        print("There are many type of birds")

    def flight(self):
        print("Most of the birds can fly")

class Sparrow():
    #Method Overriding
    def flight(self):
        print("Sparrow can fly")           


class Ostrich():
    #Method Overriding
    def flight(self):
        print("Ostrich can not can fly")  



obj_bird = Birds()
obj_sparrow = Sparrow()
obj_ostrich= Ostrich()


obj_bird.intro()
obj_bird.flight()
obj_sparrow.flight()
obj_ostrich.flight()
