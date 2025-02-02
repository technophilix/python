num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter thrid number"))


if num1 < num2 and num1 < num3:
    if num2 < num3:
        x, y, z = num1, num2, num3
    else:
        x, y, z = num1, num3, num2
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        x, y, z = num2, num1, num3
    else:
        x, y, z = num2, num3, num1
else:
    if num1 < num2:
        x, y, z = num3, num1, num2
    else:
        x, y, z = num3, num2, num1


print("Ordered numbers are {}, {}, {}".format(x, y, z))
