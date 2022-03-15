#Polymorphism with function and objects

class India:
    def capital(self):
        print("Capital of india is Delhi")
    def language(self):
        print("there is no official language in india")
    def type(self):
        print("India is developing country")


class America:
    def capital(self):
        print("Capital of india is Washington DC")
    def language(self):
        print("tLanguage of america is english")
    def type(self):
        print("India is developed country")




def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_india = India()  # creating the object of class india  
obj_america= America()    


func(obj_india)
func(obj_america)
