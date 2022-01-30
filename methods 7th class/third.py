from ast import arguments


def modify(x):
    x=15
    print(x, id(x))


x = 10 
modify(x)

print(x, id(x))


# python arguments
# 1) actual arguments
# 2) formal arguments

# python arguments
# 1) Positional arguments
# 2) Keyword argument
# 3) Default arguments
# 4) Variable length aruments

def attach(s1, s2):
    s3 = s1+s2
    print(s3)

attach('new', 'delhi')    
# attach('1','2')


def grocery(item, price=70):
    print("item= %s" %item)
    print("price= %s" %price)


grocery('sugar', 80.23)  

grocery(item='sugar', price=70.85)
grocery(price=7.85, item='sugar')
grocery(price=83.9)