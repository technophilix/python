# multiple return value

def calculator(a, b):
    c = a+b
    d = a-b
    return c, d


x, y = calculator(89, 75)
print(x)
print(y)
