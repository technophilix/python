class Myconstrutor:
    # constructor
    def __init__(self, id , name):
        self.id = id
        self.name= name
        self.display()

    def display(self):
        print(self.id)    
        print(self.name)  


mct = Myconstrutor(12, "agniswr")

# mct.id=20
# mct.name="chandra"
# mct.display()          