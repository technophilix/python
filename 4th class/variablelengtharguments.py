def add(a, *args):
    """adefinition and the objectives of the function it is a docstring"""
    print("the formal arguments", a)
    sum = a
    for i in args:
        sum = sum+i
    print(sum)


add(2, 3)
add(9, 3, 4, 5, 8, 9, 12)


# f(n) = n*f(n-1)
