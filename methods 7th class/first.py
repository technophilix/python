# function(){
# print("hello world")
# }

# function(x){

#     retrun x*x
# }

# function(str){
# print(str)
# }

# function(){

#     return x,y,z
# }



def sum(a,b):
    """this function finds sum of two numbers"""
    c = a+b
    return c

# z = sum(89.6,45.8)
# print(z)  

def fact(n):
    """ to find the value factorial n""" 
    # n = int(input("Enter a number")) 
    prod = 1
    if n == 1:
        print(1)
    else:
        while n>1:
            prod = prod*n
            n = n-1
    print(prod)
    #return n*fact(n-1)  


fact(12)


