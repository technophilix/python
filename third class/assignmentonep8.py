#find the grade of number

number = input("Enter a number")
# number = int(input("Enter a number"))
number = int(number)

if number >= 90 and number <= 100:
    print("grade A")
elif number >= 80 and number <90:
    print("grade B")
elif number >=70 and number <80:
    print("grade C")
elif number >=60 and number <70:
    print("grade D")
elif number >=0 and number <60:
    print("grade F")
else:
    print("Out of range")                    