class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
         super().__init__(first, last, pay)  #constructor overriding
         self.prog_lang = prog_lang


dev1 = Developer("Agniswar", "Chakraborty", 5000, "Python")
dev1.apply_raise()
print(dev1.prog_lang)
print(dev1.pay)
