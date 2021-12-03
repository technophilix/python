x = 100
print(x, id(x))


# Pass by object reference

def modify(b):
    b = 15
    print(b, id(b))


a = 10
modify(a)
print(a, id(a))
