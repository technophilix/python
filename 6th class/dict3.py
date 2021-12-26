#how to create a dictionary programatically
x ={}
print("Enter an numer", end=' ')
n = int(input())
for i in range(n):
    print("Enter key :", end='')
    k = input()
    print("Enter value :", end='')
    v = input()
    x.update({k:v})


print(x)

# task player and their runs in a mactch; if there are any centuries or fifties...